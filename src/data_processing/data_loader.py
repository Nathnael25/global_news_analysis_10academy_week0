import pandas as pd

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        # Load the dataset
        df = pd.read_csv(self.file_path)
        return df

if __name__ == "__main__":
    # Example usage
    loader = DataLoader('../../rating.csv')
    df = loader.load_data()

    # Explore the dataset
    print(df.head())  # Display the first few rows
    print(df.info())  # Get a concise summary of the dataset
    print(df.describe())  # Get some descriptive statistics
