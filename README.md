
# Project README

## Author
- Shikhar Saxena
- Stevens Login: ssaxena10@stevens.edu

## GitHub Repository
- [Test Harness](https://github.com/Shikhar253/CS515-PROJECT-1)

## Time Spent
- A lot!!

## Description
This project implements a Python utility that mimics the behavior of the `wc` command in Unix systems. It includes basic functionality such as counting lines, words, and characters, as well as more advanced features like support for multiple files and flags to control output information.

## Testing
To test the code, a test harness (`test.py`) has been provided. The test harness uses data-driven testing, with each test consisting of an input file and an expected output file. The tests cover various scenarios, including different combinations of flags, multiple files, and edge cases.

To run the tests, execute the following command:
```bash
$ python test.py
 ```


# Bug and Issue Log

## Bugs or Issues Encountered During Development and Testing

- **Issue 1: File Processing Error**
  - **Description:** The utility encountered errors while processing certain types of files.
  - **Resolution:** Implemented a more robust file handling mechanism to handle various file types, ensuring successful processing.

- **Issue 2: Unexpected Output Format**
  - **Description:** The utility produced unexpected output format in specific scenarios.
  - **Resolution:** Reviewed and revised the output formatting logic to align with the expected results.

## Difficult Issue Resolved

- **Issue: Memory Leak in File Parsing**
  - **Description:** The utility experienced a memory leak during the parsing of large files, leading to performance issues.
  - **Resolution:** Conducted a thorough code review, identified and optimized memory-intensive operations, and implemented efficient memory management strategies to resolve the memory leak.

# Extensions Implemented

## Extension 1: Multiple Files

- **Description:** The utility now supports processing multiple input files, providing a total count at the end.
- **Evaluation:** 
  - To test this extension, create test cases with multiple input files.
  - Compare the output with the expected results to ensure accurate counting.

## Extension 2: Flags to Control Output

- **Description:** The utility supports flags (-l, -w, -c) to control the information shown, allowing users to count only lines, words, or characters individually or in combination.
- **Evaluation:** 
  - Create test cases with different combinations of flags.
  - Verify that the output matches the expected results for each flag combination.

## Extension 3: More Advanced Gron Functionality

- **Description:** The grön utility includes an additional flag --obj that allows specifying a different base object name.
- **Evaluation:** 
  - Test the utility with different JSON input files.
  - Use the --obj flag to set a custom base object name and verify that the output reflects the specified base object name.


