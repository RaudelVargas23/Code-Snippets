import pandas as pd
import os

# Directory containing the CSV files
csv_dir = "/content/drive/MyDrive/CS 418"

# Output file for the merged CSV
merged_csv_file = "/content/drive/MyDrive/CS 418/AllYears.csv"

# List to store DataFrames from each CSV file
dataframes = []

try:
    # Iterate through CSV files in the directory
    for csv_file in os.listdir(csv_dir):
        if csv_file.endswith(".csv"):
            file_path = os.path.join(csv_dir, csv_file)
            df = pd.read_csv(file_path)
            dataframes.append(df)

    # Merge all DataFrames into a single DataFrame
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Save the merged DataFrame to a new CSV file
    merged_df.to_csv(merged_csv_file, index=False)
    print(f"Merged data saved to '{merged_csv_file}'.")

except Exception as e:
    print(f"Error merging CSV files: {e}")