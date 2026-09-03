## File Analysis and Report Generator

## Project Description

This project is a Python application that reads a `.txt` file and gives some useful information about the file.

It can count the number of lines, words, and characters. It can also find the frequency of each word and show the most frequently used word or words.

The application is menu based, so the user can choose what they want to check.

## Implemented Features

The following features are implemented in the project:

- Read a `.txt` file.
- Count the number of lines.
- Count the number of words.
- Count the number of characters.
- Find the frequency of all words.
- Search whether a particular word is present in the file.
- Find how many times a particular word appears.
- Find the most frequently used word or words.
- Display all file statistics.
- Generate a text report containing the analysis results.
- Handle some basic errors such as:
  - Empty file path
  - Empty input
  - File not found
  - Unsupported file type
  - Invalid UTF-8 text
  - Invalid menu choice

Common punctuation is removed before calculating word frequency, and words are treated without considering uppercase/lowercase differences.

## Instructions to Run the Application

### 1. Install Python

Make sure Python is installed on your system.

You can check it by running:

```bash
python --version
```

### 2. Open the Project Folder

Open a terminal and go to the project folder:

```bash
cd file-analysis-report-generator
```

### 3. Run the Application

Run the following command:

```bash
python main.py
```

### 4. Provide the Input File

When the application asks for the file path, enter the path of a `.txt` file.

Example:

```text
Data/Input/test.txt
```

After that, select an option from the menu to perform the required analysis.

To exit, select option `10`. You can also press `1` when the application asks for the input file path to exit.

## Required Packages

This project does not require any external Python packages.

It uses only Python's built-in features and the `string` module.

### Python Version

The project was developed and tested using Python 3.

## Known Limitations

- Only `.txt` files are supported.
- The input file should contain valid UTF-8 text.
- The application is command-line based and does not have a graphical interface.
- Punctuation is removed while calculating word frequency, so some punctuation-based differences are not kept.
- The character count does not include newline characters.
- The report is generated as a text file only.
- Invalid or very large file paths may still depend on the operating system's file handling.