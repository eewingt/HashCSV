import pandas as pd
import os
import datetime

# Directory containing the CSV files
directory = "C:/Users/user/Downloads/excel"

# Output file path
output_file = 'combined_file.csv'

# List to hold dataframes
dfs = []

# check if output folder exist, if not exist then create an output folder.
newpath = r'output'  # This line should be properly aligned with other code
if not os.path.exists(newpath):
    os.makedirs(newpath)
print(f'Directory "{newpath}" created successfully.')

# Iterate over all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory, filename)
        print(f'Reading {file_path}')
        df = pd.read_csv(file_path)
        dfs.append(df)

# Combine all dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Check if the file exists
if os.path.exists('output'):
    # Get the current date and time
    now = datetime.datetime.now()

    # Format the date and time
    timestamp = now.strftime('%Y%m%d_%H%M%S')
    
    # Split the file name and extension
    file_name, file_extension = os.path.splitext(file_path)
    
    # Create the new file name with the date and time
    output_file = f"{'combined_file'}_{timestamp}{file_extension}"

    csv_path = os.path.join(newpath, output_file)
    
    # Save the combined dataframe to a new CSV file
    combined_df.to_csv(csv_path, index=False)
    
    print(f"All the CSV files within the directory has been merged successfully and saved to output directory.")
else:
    print("Folder does not exist.")

