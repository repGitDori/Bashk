# File: Bashk.py

import csv
import tkinter as tk
from tkinter import filedialog

# Function to select multiple files using a Windows Explorer dialog
def select_files():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_paths = filedialog.askopenfilenames(title="Select CSV Files", filetypes=[("CSV Files", "*.csv")])
    return list(file_paths)

# Function to process Table A and remove duplicate columns based on the first row
def process_table_a(files):
    table_a = []
    sum_column_2_numerators = [0] * 40
    sum_column_2_denominators = [0] * 40
    sum_column_3_percentages = [0.0] * 40
    row_count = len(files)
    
    for file in files:
        with open(file, newline='', encoding='utf-8', errors='replace') as csvfile:
            reader = csv.reader(csvfile)
            for row_idx, row in enumerate(reader):
                if not row or all(cell.strip() == "" for cell in row):
                    print(f"Warning: Empty or incomplete row at line {row_idx+1}, skipping.")
                    continue

                if 1 <= row_idx <= 39:  # Process only rows 1 to 39 (Table A)
                    col_2_value = row[1].strip()
                    if '/' in col_2_value:
                        try:
                            num_done, num_submitted = map(int, col_2_value.split('/'))
                            sum_column_2_numerators[row_idx - 1] += num_done
                            sum_column_2_denominators[row_idx - 1] += num_submitted
                        except ValueError:
                            print(f"Warning: Invalid x/y format in row {row_idx+1}, skipping.")
                            continue

                    try:
                        percentage_value = float(row[2].rstrip('%'))
                        sum_column_3_percentages[row_idx - 1] += percentage_value
                    except ValueError:
                        print(f"Warning: Invalid percentage format in row {row_idx+1}, skipping.")
                        continue

    table_headers = None
    table_data = []

    for file in files:
        with open(file, newline='', encoding='utf-8', errors='replace') as csvfile:
            reader = csv.reader(csvfile)
            for row_idx, row in enumerate(reader):
                if 1 <= row_idx <= 40:
                    if row_idx == 1 and not table_headers:
                        table_headers = row

                    col_1_value = row[0]
                    col_last_value = row[-1]
                    
                    if sum_column_2_denominators[row_idx - 1] > 0:
                        col_2_value = f"{sum_column_2_numerators[row_idx - 1]}/{sum_column_2_denominators[row_idx - 1]}"
                    else:
                        col_2_value = "0/0"

                    avg_percentage = sum_column_3_percentages[row_idx - 1] / row_count
                    if avg_percentage == 100:
                        col_3_value = "100%"
                    else:
                        col_3_value = f"{avg_percentage:.2f}%"

                    table_data.append([col_1_value, col_2_value, col_3_value, col_last_value])

    if table_headers:
        unique_headers = []
        unique_indices = []

        for idx, header in enumerate(table_headers):
            if header not in unique_headers:
                unique_headers.append(header)
                unique_indices.append(idx)

        filtered_table_a = []
        for row in table_data:
            filtered_row = [row[i] for i in unique_indices]
            filtered_table_a.append(filtered_row)

        return filtered_table_a

    return table_a

# Function to process Table B (left unchanged)
def process_table_b(files):
    table_b = []
    
    for file in files:
        with open(file, newline='', encoding='utf-8', errors='replace') as csvfile:
            reader = csv.reader(csvfile)
            for row_idx, row in enumerate(reader):
                if not row or all(cell.strip() == "" for cell in row):
                    print(f"Warning: Empty or incomplete row at line {row_idx+1}, skipping.")
                    continue

                if row_idx >= 41:
                    table_b.append(row)

    return table_b

# Function to write the CSV files with UTF-8 encoding and BOM
def write_csv(filename, rows):
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Main function to run the tool
def main():
    files = select_files()
    table_a = process_table_a(files)
    table_b = process_table_b(files)
    write_csv('Bashk/Table_A_output.csv', table_a)
    write_csv('Bashk/Table_B_output.csv', table_b)

if __name__ == '__main__':
    main()
