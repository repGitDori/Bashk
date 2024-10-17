# File: clearAndOrganize.py

import csv

# SLA percentages you provided
sla_percentages = [
    "100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%", "100%",
    "98%", "98%", "98%", "98%", "98%", "98%", "96%", "93%", "98%", "96%",
    "98%", "98%", "98%", "96%", "93%", "96%", "93%", "96%", "93%", "98%",
    "96%", "98%", "98%", "98%", "96%", "93%", "96%", "93%"
]

# Function to read from Table_A_output.csv and create the new organized table
def organize_table_a(input_file, output_file):
    # Open the input file with UTF-8 encoding and BOM handling
    with open(input_file, newline='', encoding='utf-8', errors='replace') as csvfile:
        reader = csv.reader(csvfile)
        table_rows = list(reader)[1:38]  # Get rows 1 to 38 (skip the first row as it is usually the header)

    # Prepare the new header for the organized file
    headers = ["Field Name", "Accuracy", "Accuracy Percentage", "SLA Percentage"]

    # Open the output file to write the organized table with UTF-8 encoding and BOM
    with open(output_file, mode='w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the new header
        writer.writerow(headers)
        
        # Write the rows with the SLA Percentage populated
        for i, row in enumerate(table_rows):
            # Add the SLA percentage to the end of the row (ensure row length is 3 before adding the SLA percentage)
            writer.writerow(row[:3] + [sla_percentages[i]])

# Main function to execute the file organization
def main():
    # Input and output file paths
    input_file = 'Bashk\Table_A_output.csv'
    output_file = 'Bashk\TableA_Organized.csv'

    # Organize Table A and write to the new file
    organize_table_a(input_file, output_file)

if __name__ == "__main__":
    main()
