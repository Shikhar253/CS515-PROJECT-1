
# Project README

## Author
- Shikhar Saxena
- Stevens Login: ssaxena10@stevens.edu

## GitHub Repository
- [Test Harness](https://github.com/Shikhar253/CS515-PROJECT-1)

## Time Spent
- Around 30hrs

## Description
This project implements a Python utility that mimics the behavior of the `wc` command, 'gron' command in Unix systems along with a csv reader utility that calculates the sum of columns. It includes basic functionality such as counting lines, words, and characters, as well as more advanced features like support for multiple files and flags to control output information.

## Testing
To test the code, a test harness (`test.py`) has been provided. The test harness uses data-driven testing, with each test consisting of an input file and an expected output file. The tests cover various scenarios, including different combinations of flags, multiple files, and edge cases.

To run the tests, execute the following command:
```bash
$ python test.py
 ```


# Bug and Issue Log

## Bugs or Issues Encountered During Development and Testing

- **Issue 1: File Processing Error**
  - **Description:** The utility encountered errors while processing certain test cases for wc utility .
  - **Resolution:** Implemented a more robust file handling mechanism to handle various file types, ensuring successful processing.

- **Issue 2: Unexpected Output Format**
  - **Description:** The utility produced unexpected output format in certain scenarios.
  - **Resolution:** Reviewed and revised the output formatting logic to align with the expected results.


# Extensions Implemented

## Extension 1: Multiple Files in wc 

- **Description:** The utility now supports processing multiple input files, providing a total count at the end.
- **Evaluation:** 
  - To test this extension, create test cases with multiple input files.
  - Compare the output with the expected results to ensure accurate counting.

## Extension 2: Flags to Control Output in wc

- **Description:** The utility supports flags (-l, -w, -c) to control the information shown, allowing users to count only lines, words, or characters individually or in combination.
- **Evaluation:** 
  - Create test cases with different combinations of flags.
  - Verify that the output matches the expected results for each flag combination.

## Extension 3: More Advanced Gron Functionality 

- **Description:** The gron utility includes an additional flag --obj that allows specifying a different base object name.
- **Evaluation:** 
  - Test the utility with different JSON input files.
  - Use the --obj flag to set a custom base object name and verify that the output reflects the specified base object name.
# CSV Sum Utility

The `csv_sum` utility is a command-line tool designed to process comma-separated values (CSV) files and calculate the sum of specified columns. It provides a convenient way to perform basic numeric operations on CSV data, making it useful for tasks such as analyzing financial data, statistical datasets, or any other tabular data organized in a CSV format.

## Features

- **Column Selection:** Users can specify the columns for which they want to calculate the sum, providing flexibility in choosing the data to analyze.

## Usage

```bash
python prog/csv_sum.py input_file.csv col1 col2 ...
```

