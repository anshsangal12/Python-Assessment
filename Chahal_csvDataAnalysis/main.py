from data import Data
from operations import Numeric_Operations, String_Operations
from report import Report
import os

def get_valid_int(prompt, min_val, max_val):
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
            print(f"  Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("  Invalid input. Please enter a whole number.")

print("\n=== CSV Data Analysis and Report Generator ===\n")
while True:
    path= input("Enter the path to your CSV file: ").strip('"')
    try:
        data = Data(path)
        data.load_csv()
        if len(data.csv_matrix) == 0:
            print(" Empty File. Please try Another file.\n")
        break
    except FileNotFoundError:
        print("File Not Found. Please check the path and try again.\n")
    except PermissionError:
        print("Permission denied. Can't open the file\n")
    except Exception as e:
        print(f" Could not load file: {e}\n")

headers = data.csv_matrix[0]
headers[0] = headers[0].lstrip('ï»¿')

total_rows = len(data.csv_matrix) - 1
print(f"\n File Loaded! {total_rows} data rows found.")
report = Report(path)

while True:
    print("\nAvailable columns:")
    for i, column in enumerate(headers):
        print(f" {i + 1}. {column}")

    while True:
        try:
            column_index = int(input(f"\nEnter column number (1-{len(headers)}): "))
            if 1 <= column_index <= len(headers):
                column_index -= 1
                break
            print(f"Please enter a number between 1 and {len(headers)}.")
        except ValueError:
            print(" Invalid input. Please enter a number")

    column_name = headers[column_index]

    is_numeric = True
    while True:
        is_numeric_input = input("Analysis type - 'n' for Numeric, 's' for String: ").strip().lower()
        if is_numeric_input == 'n':
            is_numeric = True
            break
        elif is_numeric_input == 's':
            is_numeric = False
            break
        print(f"Invalid choice. Please enter 'n' or 's'.")


    start = 1
    end = total_rows + 1
    print(f"\n  Total data rows available: {total_rows}")
    while True:
        choice = input("Analyze all rows? (y/n): ").strip().lower()
        if choice == 'y':
            break
        elif choice == 'n':
            start = get_valid_int(f" Start row (1 - {total_rows}): ", 1, total_rows)
            end = get_valid_int(f" End row ({start} - {total_rows}): ", start, total_rows) + 1
            break
        print(" Please enter 'y' or 'n'.")


    if is_numeric:
        ops = Numeric_Operations(data.csv_matrix, start,end)
    else:
        ops = String_Operations(data.csv_matrix, start, end)

    print()
    section = report.generate_report(ops, column_index, column_name, is_numeric)
    print(section)

    group_choice = input("Group records by this column? (y/n)[Press 'Enter' for no]: ").strip().lower()
    if group_choice == 'y':
        groups = ops.group_records(column_index)
        section = report.add_groups_to_report(groups, column_name)
        print(section)

    again = input("Analyze another column? (y/n)[Press 'Enter' for no]: ").strip().lower()
    if again != 'y':
        break
    print()

export_choice = input("Export the full report to a file? (y/n): ").strip().lower()
if export_choice == 'y':
    while True:
        input_file_name = input(" Output file name (e.g. report): ").strip()
        try:
            output_path = fr"outputs\{input_file_name}.txt"
            if os.path.exists(output_path):
                print(f"File Named '{input_file_name}' already Exists")
                continue
            report.export_report(output_path)
            print(f" Report saved to '{output_path}'.")
            break
        except Exception as e:
            print(f" Could not save the file: {e}. Please try again")
print("\n Thanks!\n")
