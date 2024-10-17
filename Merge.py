import csv
from datetime import datetime

# Generate the filename with the current date in YYYYMMDD format
current_date = datetime.now().strftime('%Y%m%d')
output_file = f'Bashk_{current_date}.csv'

# Define input file names
table_a_file = 'Bashk\TableA_Organized.csv'
table_b_file = 'Bashk\TableB_Organized.csv'

# Open the output file in write mode with UTF-8 BOM encoding
with open(output_file, mode='w', newline='', encoding='utf-8-sig') as outfile:
    writer = csv.writer(outfile)
    
    # Read and write TableA_Organized.csv with UTF-8 encoding
    with open(table_a_file, mode='r', encoding='utf-8', errors='replace') as file_a:
        reader_a = csv.reader(file_a)
        for row in reader_a:
            writer.writerow(row)

    # Write an empty row to separate the two tables
    writer.writerow([])

    # Read and write TableB_Organized.csv with UTF-8 encoding
    with open(table_b_file, mode='r', encoding='utf-8', errors='replace') as file_b:
        reader_b = csv.reader(file_b)
        for row in reader_b:
            writer.writerow(row)

print(f"Merged file '{output_file}' has been created successfully.")
