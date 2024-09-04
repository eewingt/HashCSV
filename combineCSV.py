import pandas as pd
import os
import datetime

# Directory containing the CSV files
directory = "C:/Users/leslietoh/Downloads/excel"

# Output file path
output_file = 'combined_file.csv'

# List to hold dataframes
dfs = []


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
    
    #create a output folder

    csv_path = os.path.join(newpath, output_file)
    
    # Save the combined dataframe to a new CSV file
    combined_df.to_csv(csv_path, index=False)
    
    print(f"Folder exists")
else:
    print("Folder does not exist.")

print(f'Combined file saved to {output_file}')

csv_directory = newpath + '/' + output_file

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_directory)

# Filter the DataFrame based on the conditions
filtered_df = df[(df.iloc[:, 1] == 'normal') & (df.iloc[:, 2] == 'SFF')]
filtered_df1 = df[(df.iloc[:, 1] == 'spam') & (df.iloc[:, 2] == 'SFF')]
filtered_df2 = df[(df.iloc[:, 1] == 'phish') & (df.iloc[:, 2] == 'SFF')]
filtered_df3 = df[(df.iloc[:, 1] == 'normal') & (df.iloc[:, 2] == 'DLL')]
filtered_df4 = df[(df.iloc[:, 1] == 'spam') & (df.iloc[:, 2] == 'DLL')]
filtered_df5 = df[(df.iloc[:, 1] == 'phish') & (df.iloc[:, 2] == 'DLL')]
filtered_df6 = df[(df.iloc[:, 1] == 'normal') & (df.iloc[:, 2] == 'MPH')]
filtered_df7 = df[(df.iloc[:, 1] == 'spam') & (df.iloc[:, 2] == 'MPH')]
filtered_df8 = df[(df.iloc[:, 1] == 'phish') & (df.iloc[:, 2] == 'MPH')]
filtered_df9 = df[(df.iloc[:, 1] == 'normal') & (df.iloc[:, 2] == 'HSV')]
filtered_df10 = df[(df.iloc[:, 1] == 'spam') & (df.iloc[:, 2] == 'HSV')]
filtered_df11 = df[(df.iloc[:, 1] == 'phish') & (df.iloc[:, 2] == 'HSV')]


# Count the number of rows that meet the conditions
countSFF_normal = filtered_df.shape[0]
countSFF_spam = filtered_df1.shape[0]
countSFF_phish = filtered_df2.shape[0]
countDLL_normal = filtered_df3.shape[0]
countDLL_spam = filtered_df4.shape[0]
countDLL_phish = filtered_df5.shape[0]
countMPH_normal = filtered_df6.shape[0]
countMPH_spam = filtered_df7.shape[0]
countMPH_phish = filtered_df8.shape[0]
countHSV_normal = filtered_df9.shape[0]
countHSV_spam = filtered_df10.shape[0]
countHSV_phish = filtered_df11.shape[0]

# Print the result (optional)
print(f'Number of rows where type is "spam" and domain is "SFF": {countHSV_phish}')

