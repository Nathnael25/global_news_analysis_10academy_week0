import pandas as pd
from src.data_processing.data_loader import DataLoader

# Load the dataset
loader = DataLoader('../../rating.csv')
df = loader.load_data()

# Explore the dataset
print(df.head())  # Display the first few rows
print(df.info())  # Get a concise summary of the dataset
print(df.describe())  # Get some descriptive statistics
