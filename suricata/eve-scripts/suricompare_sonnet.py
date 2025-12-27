#!/usr/bin/env python3
"""
Verify Suricata data integrity across JSON, Parquet, and DuckDB formats
"""

import json
import polars as pl
import duckdb
from pathlib import Path
import sys
from typing import Dict, Any
import hashlib

class DataVerifier:
    def __init__(self, json_file: str, parquet_file: str, duckdb_file: str):
        self.json_file = Path(json_file)
        self.parquet_file = Path(parquet_file)
        self.duckdb_file = Path(duckdb_file)
        
    def verify_file_exists(self):
        """Check if all files exist"""
        print("=" * 60)
        print("FILE EXISTENCE CHECK")
        print("=" * 60)
        
        for file in [self.json_file, self.parquet_file, self.duckdb_file]:
            exists = file.exists()
            size = file.stat().st_size / (1024**3) if exists else 0  # Size in GB
            print(f"{'✓' if exists else '✗'} {file.name}: {size:.2f} GB")
            if not exists:
                print(f"ERROR: {file} does not exist!")
                sys.exit(1)
        print()
    
    def count_json_records(self, sample_size: int = 1000000) -> int:
        """Count records in JSON file (NDJSON format assumed)"""
        print("Counting JSON records (sampling approach)...")
        
        # Sample first N lines to estimate
        line_count = 0
        with open(self.json_file, 'r') as f:
            for i, _ in enumerate(f):
                line_count += 1
                if i >= sample_size:
                    break
        
        # If we read fewer lines than sample_size, we have exact count
        if line_count < sample_size:
            print(f"  JSON total records (exact): {line_count:,}")
            return line_count
        
        # Otherwise, estimate based on file size
        file_size = self.json_file.stat().st_size
        with open(self.json_file, 'r') as f:
            sample_lines = [next(f) for _ in range(min(10000, line_count))]
        
        avg_line_size = sum(len(line) for line in sample_lines) / len(sample_lines)
        estimated_count = int(file_size / avg_line_size)
        
        print(f"  JSON estimated records: ~{estimated_count:,}")
        return estimated_count
    
    def get_parquet_info(self) -> Dict[str, Any]:
        """Get Parquet file information"""
        print("=" * 60)
        print("PARQUET FILE ANALYSIS")
        print("=" * 60)
        
        df = pl.scan_parquet(self.parquet_file)
        
        # Get row count
        row_count = df.select(pl.count()).collect().item()
        print(f"Total records: {row_count:,}")
        
        # Get schema
        schema = df.collect_schema()
        print(f"\nSchema ({len(schema)} columns):")
        for col_name, dtype in schema.items():
            print(f"  - {col_name}: {dtype}")
        
        return {
            'row_count': row_count,
            'schema': schema,
            'column_names': list(schema.keys())
        }
    
    def get_duckdb_info(self) -> Dict[str, Any]:
        """Get DuckDB file information"""
        print("\n" + "=" * 60)
        print("DUCKDB FILE ANALYSIS")
        print("=" * 60)
        
        conn = duckdb.connect(str(self.duckdb_file), read_only=True)
        
        # Get table names
        tables = conn.execute("SHOW TABLES").fetchall()
        print(f"Tables found: {[t[0] for t in tables]}")
        
        if not tables:
            print("ERROR: No tables found in DuckDB!")
            sys.exit(1)
        
        table_name = tables[0][0]  # Use first table
        print(f"Using table: {table_name}")
        
        # Get row count
        row_count = conn.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
        print(f"Total records: {row_count:,}")
        
        # Get schema
        schema_info = conn.execute(f"DESCRIBE {table_name}").fetchall()
        print(f"\nSchema ({len(schema_info)} columns):")
        schema = {}
        for col_name, col_type, *_ in schema_info:
            schema[col_name] = col_type
            print(f"  - {col_name}: {col_type}")
        
        conn.close()
        
        return {
            'row_count': row_count,
            'schema': schema,
            'column_names': list(schema.keys()),
            'table_name': table_name
        }
    
    def sample_json_records(self, n: int = 10) -> list:
        """Get sample records from JSON at different positions"""
        n = max(n, 3)  # Ensure we always sample first/middle/last
        print("\n" + "=" * 60)
        print(f"SAMPLING {n} JSON RECORDS")
        print("=" * 60)
        
        samples = []
        
        # Get first record
        with open(self.json_file, 'r') as f:
            first_line = f.readline()
            samples.append(('first', json.loads(first_line)))
            print(f"✓ Got first record")
        
        # Get middle record(s)
        file_size = self.json_file.stat().st_size
        positions = [file_size * i // (n + 1) for i in range(1, n - 1)]
        
        with open(self.json_file, 'rb') as f:
            for i, pos in enumerate(positions):  # Leave room for first and last
                f.seek(pos)
                f.readline()  # Skip partial line
                line = f.readline()
                if line:
                    try:
                        samples.append((f'middle_{i+1}', json.loads(line)))
                        print(f"✓ Got middle record {i+1}")
                    except json.JSONDecodeError:
                        print(f"✗ Could not parse middle record {i+1}")
        
        # Get last record
        with open(self.json_file, 'rb') as f:
            f.seek(-min(10000, file_size), 2)  # Seek near end
            lines = f.readlines()
            if lines:
                try:
                    samples.append(('last', json.loads(lines[-1])))
                    print(f"✓ Got last record")
                except json.JSONDecodeError:
                    print(f"✗ Could not parse last record")
        
        return samples
    
    def compare_sample_records(self, json_samples: list, parquet_info: Dict, duckdb_info: Dict):
        """Compare sample records across formats"""
        print("\n" + "=" * 60)
        print("SPOT CHECK: COMPARING SAMPLE RECORDS")
        print("=" * 60)
        
        id_fields = ['flow_id', 'timestamp', 'event_type']
        df_parquet = pl.scan_parquet(self.parquet_file)
        conn = duckdb.connect(str(self.duckdb_file), read_only=True)
        
        for label, record in json_samples:
            identifier = {f: record[f] for f in id_fields if f in record}
            if not identifier:
                print(f"\n{label}: No identifier fields found, skipping comparison.")
                continue
            
            print(f"\n{label}: Using identifier {identifier}")
            
            # Parquet lookup
            print("  📊 Parquet...")
            query = df_parquet
            for field, value in identifier.items():
                if field in parquet_info['column_names']:
                    query = query.filter(pl.col(field) == value)
            parquet_match = query.collect()
            if len(parquet_match) > 0:
                print(f"  ✓ Found ({len(parquet_match)} matches)")
                print(f"  Sample: {parquet_match.head(1).to_dicts()[0]}")
            else:
                print("  ✗ Not found (could be expected with sampling)")
            
            # DuckDB lookup
            print("  📊 DuckDB...")
            where_clause = " AND ".join(
                [f"{k} = '{v}'" if isinstance(v, str) else f"{k} = {v}"
                 for k, v in identifier.items()
                 if k in duckdb_info['column_names']]
            )
            if not where_clause:
                print("  ✗ No matching columns in DuckDB schema, skipping.")
                continue
            
            query = f"SELECT * FROM {duckdb_info['table_name']} WHERE {where_clause} LIMIT 1"
            try:
                duckdb_match = conn.execute(query).fetchall()
                if duckdb_match:
                    print(f"  ✓ Found ({len(duckdb_match)} matches)")
                    print(f"  Sample: {duckdb_match[0][:5]}...")
                else:
                    print("  ✗ Not found (could be expected with sampling)")
            except Exception as e:
                print(f"  ✗ Error querying DuckDB: {e}")
        
        conn.close()
    
    def verify_record_counts(self, json_count: int, parquet_info: Dict, duckdb_info: Dict):
        """Compare record counts across formats"""
        print("\n" + "=" * 60)
        print("RECORD COUNT COMPARISON")
        print("=" * 60)
        
        counts = {
            'JSON (estimated)': json_count,
            'Parquet': parquet_info['row_count'],
            'DuckDB': duckdb_info['row_count']
        }
        
        for format_name, count in counts.items():
            print(f"{format_name:20s}: {count:,}")
        
        # Check if Parquet and DuckDB match
        if parquet_info['row_count'] == duckdb_info['row_count']:
            print(f"\n✓ Parquet and DuckDB record counts MATCH")
        else:
            diff = abs(parquet_info['row_count'] - duckdb_info['row_count'])
            print(f"\n✗ Parquet and DuckDB differ by {diff:,} records")
        
        # Check if close to JSON estimate
        json_parquet_diff = abs(json_count - parquet_info['row_count'])
        json_parquet_pct = (json_parquet_diff / json_count * 100) if json_count > 0 else 0
        
        if json_parquet_pct < 5:  # Within 5%
            print(f"✓ Parquet count is within 5% of JSON estimate ({json_parquet_pct:.2f}%)")
        else:
            print(f"⚠ Parquet count differs from JSON estimate by {json_parquet_pct:.2f}%")
   
    def verify_schemas(self, parquet_info: Dict, duckdb_info: Dict):
        """Compare schemas between Parquet and DuckDB"""
        print("\n" + "=" * 60)
        print("SCHEMA COMPARISON")
        print("=" * 60)
        
        parquet_cols = set(parquet_info['column_names'])
        duckdb_cols = set(duckdb_info['column_names'])
        
        if parquet_cols == duckdb_cols:
            print(f"✓ Column names MATCH ({len(parquet_cols)} columns)")
        else:
            print(f"✗ Column names DIFFER")
            
            only_parquet = parquet_cols - duckdb_cols
            only_duckdb = duckdb_cols - parquet_cols
            
            if only_parquet:
                print(f"\n  Only in Parquet: {only_parquet}")
            if only_duckdb:
                print(f"  Only in DuckDB: {only_duckdb}")
        
        # Check common columns
        common_cols = parquet_cols & duckdb_cols
        print(f"\nCommon columns: {len(common_cols)}")
        
        # Sample a few column types
        print("\nSample column type comparison:")
        for col in list(common_cols)[:10]:  # First 10 common columns
            parquet_type = str(parquet_info['schema'][col])
            duckdb_type = str(duckdb_info['schema'][col])
            match = "✓" if parquet_type.lower() in duckdb_type.lower() or \
                           duckdb_type.lower() in parquet_type.lower() else "✗"
            # Use ljust() instead of format string width specifier
            col_padded = col.ljust(30)
            parquet_padded = parquet_type.ljust(15)
            print(f"  {match} {col_padded}: Parquet={parquet_padded} | DuckDB={duckdb_type}")
    
    def run_verification(self):
        """Run complete verification"""
        print("\n" + "=" * 60)
        print("SURICATA DATA VERIFICATION")
        print("=" * 60 + "\n")
        
        # Step 1: Verify files exist
        self.verify_file_exists()
        
        # Step 2: Get info from all formats
        print("Analyzing Parquet file...")
        parquet_info = self.get_parquet_info()
        
        print("\nAnalyzing DuckDB file...")
        duckdb_info = self.get_duckdb_info()
        
        print("\nEstimating JSON record count...")
        json_count = self.count_json_records()
        
        # Step 3: Verify record counts
        self.verify_record_counts(json_count, parquet_info, duckdb_info)
        
        # Step 4: Verify schemas
        self.verify_schemas(parquet_info, duckdb_info)
        
        # Step 5: Sample and compare records
        json_samples = self.sample_json_records(n=10)
        self.compare_sample_records(json_samples, parquet_info, duckdb_info)
        
        # Final summary
        print("\n" + "=" * 60)
        print("VERIFICATION COMPLETE")
        print("=" * 60)
        print("\n✓ All verification checks completed!")
        print("  Review the output above for any warnings or errors.")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python verify_data.py <json_file> <parquet_file> <duckdb_file>")
        print("\nExample:")
        print("  python verify_data.py suricata.json suricata.parquet suricata.db")
        sys.exit(1)
    
    json_file = sys.argv[1]
    parquet_file = sys.argv[2]
    duckdb_file = sys.argv[3]
    
    verifier = DataVerifier(json_file, parquet_file, duckdb_file)
    verifier.run_verification()
