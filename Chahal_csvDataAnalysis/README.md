# CSV Data Analysis and Report Generator

## Project Description
This is a Python command-line application designed to read, process, and analyze data from CSV files. It provides an interactive interface for users to select specific columns and row ranges, validates the data, and generates statistical reports based on whether the data is numeric or text-based.

## Implemented Features
* **File Handling:** Loads data from a user-specified CSV file with basic error handling for missing or inaccessible files.
* **Data Validation:** Checks data for validity, automatically filtering out missing or mismatched types (e.g., text in a numeric column).
* **Numeric Analysis:** Calculates Total, Average, Highest, Lowest, and Median values for numerical columns.
* **String Analysis:** Calculates Most Occurring, Least Occurring, and Total Unique values for text columns.
* **Data Grouping:** Can group the dataset by unique values in any selected column.
* **Export functionality:** Allows the user to save the final accumulated report to a `.txt` file.

## Instructions to Run the Application
1. Ensure you have Python installed on your system.
2. Open your terminal or command prompt.
3. Navigate to the folder containing the project files.
4. Run the following command:
   ```bash
   python main.py
   ```
5. Follow the on-screen prompts. When asked for a file path, enter the location of your CSV file (e.g., `students.csv` or `C:\path\to\your\file.csv`).

## Required Packages
This project relies entirely on the Python Standard Library. No external installations or `pip` packages are required. 
* `csv` (for reading the file)
* `collections` (specifically `defaultdict` for string analysis)

## Known Limitations
* **Delimiter:** The application currently has a hardcoded comma (`;`) delimiter for CSV parsing. It will not properly format semicolon-separated files unless the code is modified.
* **Memory Usage:** The application loads the entire CSV matrix into memory (as a 2D list). While fine for normal assignments, it could struggle with extremely large datasets.
* **Headers:** The application assumes that the very first row of the provided CSV file is a header row containing column names.
* **Encoding:** The application assumes that the input file is encoded using `cp1252`.