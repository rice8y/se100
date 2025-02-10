import argparse
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

LIGHTRED_BG = "\033[48;2;255;100;100m"
LIGHTGREEN_BG = "\033[48;2;100;203;50m"
DARKRED_BG = "\033[48;2;255;50;50m"
DARKGREEN_BG = "\033[48;2;0;153;0m"

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
                before_hl = f"{Fore.WHITE}{LIGHTRED_BG}{line}"
                before_hl = line.replace(before, f"{DARKRED_BG}{before}{Fore.WHITE}{LIGHTRED_BG}")
                after_hl = f"{Fore.WHITE}{LIGHTGREEN_BG}{line}"
                after_hl = line.replace(before, f"{DARKGREEN_BG}{after}{Fore.WHITE}{LIGHTGREEN_BG}")

                print(f"{Fore.WHITE}{LIGHTRED_BG}- {before_hl}{Style.RESET_ALL}", end='')
                print(f"{Fore.WHITE}{LIGHTGREEN_BG}+ {after_hl}{Style.RESET_ALL}", end='')
                
    if not flag:
        raise ValueError(f"Error: '{before}' was not found in '{file}'.")

def main():
    args = parse_args()
    diff(args.file, args.before, args.after)

if __name__ == "__main__":
    main()
