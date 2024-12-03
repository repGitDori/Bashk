import csv
import tkinter as tk
from tkinter import filedialog
import os

def split_csv_into_tables(input_file):
    table_a_data = []
    table_b_data = []
    current_table = table_a_data
    separator_found = False

    with open(input_file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            # Check for two or more consecutive empty fields (commas)
            empty_field_count = 0
            for field in row:
                if field == '':
                    empty_field_count += 1
                else:
                    empty_field_count = 0

                if empty_field_count >= 2:
                    separator_found = True
                    break

            if separator_found:
                current_table = table_b_data
                separator_found = False
                continue

            current_table.append(row)

    return table_a_data, table_b_data

def main():
    # Hide the root Tkinter window
    root = tk.Tk()
    root.withdraw()

    # Open file dialog to select multiple CSV files
    file_paths = filedialog.askopenfilenames(
        title='Select CSV files',
        filetypes=[('CSV Files', '*.csv')]
    )

    for file_path in file_paths:
        table_a, table_b = split_csv_into_tables(file_path)

        # Get the base name of the file without extension
        base_name = os.path.splitext(os.path.basename(file_path))[0]

        # Define output file paths
        output_a = os.path.join(os.path.dirname(file_path), f'{base_name}_table_A_Stat.csv')
        output_b = os.path.join(os.path.dirname(file_path), f'{base_name}_table_B_Changes.csv')

        # Write Table A Stat to a new CSV file
        with open(output_a, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(table_a)

        # Write Table B Changes to a new CSV file
        with open(output_b, 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(table_b)

        print(f'Processed "{file_path}" and created:')
        print(f' - {output_a}')
        print(f' - {output_b}\n')

if __name__ == "__main__":
    main()
