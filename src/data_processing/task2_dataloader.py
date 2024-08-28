import pandas as pd

def load_news_data(file_path='data.csv'):
    """
    Load the news data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing the news data.

    Returns:
    pd.DataFrame: The loaded data as a pandas DataFrame.
    """
    # Load the data
    data = pd.read_csv(file_path)
    
    # Preview the data
    print("Data Preview:")
    print(data.head())
    
    return data

# Example usage
if __name__ == '__main__':
    # Load the data and preview
    data = load_news_data()
