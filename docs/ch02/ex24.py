import pandas as pd
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Save iris dataset in CSV format for each class.")
    parser.add_argument("--file", type=str, required=True, help="Path to the input file.")
    return parser.parse_args()

def save_csv(file):
    try:
        df = pd.read_csv(file)
        setosa_df = df[df["class"] == "Iris-setosa"].drop("class", axis=1)
        versicolor_df = df[df["class"] == "Iris-versicolor"].drop("class", axis=1)
        virginica_df = df[df["class"] == "Iris-virginica"].drop("class", axis=1)
        
        setosa_df.to_csv("Iris-setosa.csv",index=False)
        versicolor_df.to_csv("Iris-versicolor.csv",index=False)
        virginica_df.to_csv("Iris-virginica.csv",index=False)

    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return None
        
def main():
    args = parse_args()
    save_csv(args.file)

if __name__ == "__main__":
    main()