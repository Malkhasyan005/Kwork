import pandas as pd

input_file = "data/raw_data.csv"
output_file = "data/cleaned_data.csv"

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    
    required_columns = ["Name", "Income"]
    available_columns = [col for col in required_columns if col in df.columns]
    
    if available_columns:
        df.dropna(subset=available_columns, inplace=True)
    
    if "Age" in df.columns:
        df['Age'].fillna(df['Age'].mean(), inplace=True)
    
    df.drop_duplicates(inplace=True)
    
    if "Income" in df.columns:
        df["Income"] = pd.to_numeric(df["Income"], errors='coerce')
    
    df.to_csv(output_file, index=False)
    print(f"Data cleaned and saved to {output_file}")

clean_data(input_file, output_file)