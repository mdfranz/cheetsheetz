import argparse
import duckdb
import polars as pl
import json
import random
import os

def sample_duckdb(con, table, n):
    query = f"SELECT * FROM {table} USING SAMPLE {n} ROWS"
    return con.execute(query).fetchdf()

def sample_json_lines(path, n):
    offsets = []
    with open(path, "r") as f:
        while True:
            off = f.tell()
            line = f.readline()
            if not line:
                break
            offsets.append(off)

    n = min(n, len(offsets))
    chosen = random.sample(offsets, n)

    rows = []
    with open(path, "r") as f:
        for off in chosen:
            f.seek(off)
            rows.append(json.loads(f.readline()))

    return pl.DataFrame(rows)

def check_rows_in_parquet(df, parquet_path):
    pq_lazy = pl.scan_parquet(parquet_path)
    missing = []

    for row in df.iterrows(named=True):
        expr = None
        for col, val in row.items():
            cond = pl.col(col) == val
            expr = cond if expr is None else (expr & cond)

        exists = pq_lazy.filter(expr).limit(1).collect()
        if exists.height == 0:
            missing.append(row)

    return missing

def main():
    parser = argparse.ArgumentParser(description="Sample and compare DuckDB, Parquet, and optionally JSON")
    parser.add_argument("--db", required=True)
    parser.add_argument("--table", required=True)
    parser.add_argument("--parquet", required=True)
    parser.add_argument("--json")
    parser.add_argument("--n", type=int, required=True, help="Number of rows to sample")

    args = parser.parse_args()

    con = duckdb.connect(args.db)
    con.execute("PRAGMA threads=8")

    # Sample DuckDB
    print(f"\nSampling {args.n} rows from DuckDB table {args.table}...")
    db_sample = sample_duckdb(con, args.table, args.n)
    print("Sample complete")

    # Check against Parquet
    print("Checking sampled rows against Parquet...")
    missing = check_rows_in_parquet(db_sample, args.parquet)
    print("Missing from Parquet:", len(missing))
    if missing:
        print("Example missing row:", missing[0])

    # Optional JSON sample
    if args.json:
        print(f"\nSampling {args.n} rows from JSON file...")
        json_sample = sample_json_lines(args.json, args.n)
        print("Checking JSON sample against Parquet...")
        missing_json = check_rows_in_parquet(json_sample, args.parquet)
        print("Missing JSON rows in Parquet:", len(missing_json))
        if missing_json:
            print("Example missing JSON row:", missing_json[0])

    print("\nDone")

if __name__ == "__main__":
    main()
