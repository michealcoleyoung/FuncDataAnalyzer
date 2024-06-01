# - Implement a function to load data from CSV files.
# - Ensure error handling for file not found or invalid format.
# - Write unit tests for the data loading function.
import pandas as pd
import os


def data_loader(file_name):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', file_name)

    try:
        data = pd.read_csv(str(file_path))
        return data
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_name} is empty.")
        return None
    except FileNotFoundError:
        print(f"Error: File '{file_name}'could not be found.")
        return None
    except pd.errors.ParserError:
        print(f"Error: {file_name} is not a valid CSV file. Please provide a CSV file.")
        return None