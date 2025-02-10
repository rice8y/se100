import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Check the number of lines in the input file.")
    parser.add_argument("--file", type=str, required=True, required=True, help="Path to the input file.")
    return parser.parse_args()

def count_lines(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return None
        
def main():
    args = parse_args()
    line_cnt = count_lines(args.file)
    if line_cnt is not None:
        print(f"Number of lines: {line_cnt}")

if __name__ == "__main__":
    main()