import argparse
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def parse_args():
    parser = argparse.ArgumentParser(description="Search for lines containing a target string in a file.")
    parser.add_argument("--file", type=str, help="Path to the input file.")
    parser.add_argument("--tgt", type=str, help="Target string to search for in the file.")
    return parser.parse_args()
    
def grep(file, tgt):
    flag = False
    with open(file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            if tgt in line:
                flag = True
                highlighted = line.replace(tgt, f"{Fore.RED}{tgt}{Style.RESET_ALL}")
                print(f"Line {i}: {highlighted}", end='')
                
    if not flag:
        raise ValueError(f"Error: '{tgt}' was not found in '{file}'.")

def main():
    args = parse_args()
    grep(args.file, args.tgt)
    
if __name__ == "__main__":
    main()
