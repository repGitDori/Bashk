# File: clearAndOrganize_TableB.py

import csv

# Function to read from Table_B_output.csv and create the new organized table
def organize_table_b(input_file, output_file):
    # Open the input file with UTF-8 encoding and handle potential encoding errors
    with open(input_file, newline='', encoding='utf-8', errors='replace') as csvfile:
        reader = csv.reader(csvfile)
        table_rows = list(reader)  # Read all rows from Table_B_output.csv

    # Prepare the new header for the organized file
    headers = ["DGS_Image_Record", "Field", "Data", "Notes"]

    # Open the output file to write the organized table with UTF-8 encoding and BOM
    with open(output_file, mode='w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the new header
        writer.writerow(headers)
        
        # Write the rows from Table B into the new file
        for row in table_rows:
            writer.writerow(row)

# Main function to execute the file organization
def main():
    # Input and output file paths
    input_file = 'Bashk\Table_B_output.csv'
    output_file = 'Bashk\TableB_Organized.csv'

    # Organize Table B and write to the new file
    organize_table_b(input_file, output_file)

if __name__ == "__main__":
    main()
