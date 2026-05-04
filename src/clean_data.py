import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Convert date column
    df['date'] = pd.to_datetime(df['date'])

    # Add revenue column
    df['revenue'] = df['price'] * df['quantity']

    return df

if __name__ == "__main__":
    df = clean_data("data/sales.csv")
    print(df.head())