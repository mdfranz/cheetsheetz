import polars as pl
import sys
import os

def convert_json_to_parquet():
    # 1. Check if an argument was provided
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_file.json>")
        sys.exit(1)

    input_file = sys.argv[1]
    
    # 2. Automatically generate output filename
    # e.g., "data.json" becomes "data.parquet"
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.parquet"

    print(f"Converting: {input_file}")
    print(f"Destination: {output_file}")
    print("-" * 30)

    try:
        # 3. Lazy Scan & Stream
        q = pl.scan_ndjson(input_file, infer_schema_length=50000)

        q.sink_parquet(
            output_file, 
            compression="zstd",
            compression_level=5,
            row_group_size=1_000_000, 
            maintain_order=True
        )
        
        # 4. Final stats
        orig_size_gb = os.path.getsize(input_file) / (1024**3)
        new_size_gb = os.path.getsize(output_file) / (1024**3)
        
        print(f"Success!")
        print(f"Original Size: {orig_size_gb:.2f} GB")
        print(f"Parquet Size:  {new_size_gb:.2f} GB")

    except Exception as e:
        print(f"\nError: {e}")
        print("Tip: Ensure your input is Newline Delimited JSON (NDJSON).")

if __name__ == "__main__":
    convert_json_to_parquet()
