import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Displays details of the input file.")
    parser.add_argument("--file", type=str, required=True, help="Path to the input file.")
    return parser.parse_args()

def print_info(file):
    try:
        df = pd.read_csv(file)
        rows = df.shape[0]
        cols = df.shape[1]
        header = df.columns.tolist()
        print(f"Number of lines: {rows}\nNumber of items: {cols}")
        for i, item in enumerate(header, start=1):
            print(f"Item {i}: {item}")
        
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return None
        
def main():
    args = parse_args()
    print_info(args.file)

if __name__ == "__main__":
    main()