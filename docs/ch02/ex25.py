import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Displays the JSON file.")
    parser.add_argument("--file", type=str, required=True, help="Path to the input file.")
    return parser.parse_args()

def print_json(file):
    try:
        df = pd.read_json(file)
        rows = df.shape[0]
        print(f"Number of lines: {rows}")
        print("\nData:")
        print(df.to_string(index=False))

    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return None
        
def main():
    args = parse_args()
    print_json(args.file)

if __name__ == "__main__":
    main()