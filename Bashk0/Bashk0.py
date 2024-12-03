import csv
#stage one
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

# Replace 'your_input_file.csv' with the path to your CSV file
table_a, table_b = split_csv_into_tables('your_input_file.csv')

# Write Table A Stat to a new CSV file
with open('table_A_Stat.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(table_a)

# Write Table B Changes to a new CSV file
with open('table_B_Changes.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(table_b)
