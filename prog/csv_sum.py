#!/usr/bin/env python
import csv
import sys
def sum_columns(csv_file, columns):
    """
    Load a CSV file and sum specified columns.

    Parameters:
    - csv_file (str): Path to the CSV file.
    - columns (list): List of column indices to sum.

    Returns:
    - list: Sums of specified columns.
    """
    sums = [0] * len(columns)

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            for i, col in enumerate(columns):
                try:
                    value = float(row[col])
                    sums[i] += value
                except (ValueError, IndexError):
                    pass

    return sums
def main():
    try:
        if len(sys.argv) < 3:
            raise ValueError("Usage: python csv_sum.py <csv_file> <column1> [column2 ...]")
        csv_file = sys.argv[1]
        columns = [int(col) for col in sys.argv[2:]]
        sums = sum_columns(csv_file, columns)
        print(f"Sums of specified columns {columns}: {sums}")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
