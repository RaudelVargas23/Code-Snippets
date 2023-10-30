import pandas as pd
import os

# Directory containing the Excel files
excel_files_dir = "/content/drive/MyDrive/CS 418/Excel Sheets/2005-2010"

# Directory to save CSV files
output_dir = "/content/drive/MyDrive/CS 418/CSVs/2005-2010"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

try:
    # Iterate through files in the directory
    for excel_file in os.listdir(excel_files_dir):
        if excel_file.endswith(".xlsx") or excel_file.endswith(".xls"):  # Check for Excel files
            xls = pd.ExcelFile(os.path.join(excel_files_dir, excel_file))
            sheet_names = xls.sheet_names

            for sheet_name in sheet_names:
                try:
                    df = pd.read_excel(xls, sheet_name)
                    csv_filename = os.path.join(output_dir, excel_file.split(".")[0] + "_" + sheet_name + ".csv")
                    df.to_csv(csv_filename, index=False)
                    print(f"Converted '{sheet_name}' from '{excel_file}' to CSV.")
                except Exception as e:
                    print(f"Error converting '{sheet_name}' from '{excel_file}' to CSV: {e}")
except Exception as e:
    print(f"Error processing Excel files: {e}")

print("Conversion completed.")
