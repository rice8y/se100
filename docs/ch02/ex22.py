import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Display input file with line numbers.")
    parser.add_argument("--file", type=str, help="Path to the input file.")
    return parser.parse_args()

def print_lnum(file):
    try:
        with open(file, 'r') as f:
            for i, line in enumerate(f, start=1):
                print(f"{i:>2}: {line}", end='')
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return None
        
def main():
    args = parse_args()
    print_lnum(args.file)

if __name__ == "__main__":
    main()