import pandas as pd

def load_news_data(file_path='../data.csv'):

    try:
        # Load the data from the specified CSV file
        data = pd.read_csv(file_path)
        
        # Basic data checks
        if data.empty:
            raise ValueError("The loaded data is empty.")

        # Ensure necessary columns exist
        required_columns = ['title', 'content', 'published_at']
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Missing required column: {column}")

        # Drop rows where 'title' or 'content' is missing
        data.dropna(subset=['title', 'content'], inplace=True)

        # Convert 'published_at' to datetime format if it's not already
        if not pd.api.types.is_datetime64_any_dtype(data['published_at']):
            data['published_at'] = pd.to_datetime(data['published_at'], errors='coerce')

        # Drop any rows with invalid datetime values
        data.dropna(subset=['published_at'], inplace=True)

        # Optional: Reset index after dropping rows
        data.reset_index(drop=True, inplace=True)

        # Return the loaded and preprocessed data as a DataFrame
        return data
    
    except FileNotFoundError as e:
        print(f"Error: The file at {file_path} was not found.")
        raise e
    
    except pd.errors.EmptyDataError as e:
        print(f"Error: The file at {file_path} is empty or does not contain valid data.")
        raise e
    
    except Exception as e:
        print(f"An unexpected error occurred while loading the file at {file_path}: {str(e)}")
        raise e
"""
# Example usage:
if __name__ == '__main__':
    # Load the data and preview it
    data = load_news_data('data.csv')
    print(data.head())
"""

