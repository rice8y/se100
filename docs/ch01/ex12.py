import argparse
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def parse_args():
    parser = argparse.ArgumentParser(description="Search for lines containing a target string and replace it with another string.")
    parser.add_argument("--file", type=str, help="Path to the input file.")
    parser.add_argument("--before", type=str, help="String to be replaced.")
    parser.add_argument("--after", type=str, help="String to replace with.")
    return parser.parse_args()

def diff(file, before, after):
    flag = False
    with open(file, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, start=1):
            print(line, end='')
            if before in line:
                flag = True
                before_hl = line.replace(before, f"{Fore.RED}{before}{Style.RESET_ALL}")
                after_hl = line.replace(before, f"{Fore.GREEN}{after}{Style.RESET_ALL}")
                print(f"{Fore.RED}-{Style.RESET_ALL} {before_hl}", end='')
                print(f"{Fore.GREEN}+{Style.RESET_ALL} {after_hl}", end='')
                
    if not flag:
        raise ValueError(f"Error: '{before}' was not found in '{file}'.")
    else:
        print()
        
def main():
    args = parse_args()
    diff(args.file, args.before, args.after)

if __name__ == "__main__":
    main()