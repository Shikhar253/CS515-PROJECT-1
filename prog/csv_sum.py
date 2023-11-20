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
                    # Ignore non-numeric values or index errors
                    pass

    return sums

def main():
    try:
        # Input file and columns to sum are specified as command line arguments
        if len(sys.argv) < 3:
            raise ValueError("Usage: python csv_sum.py <csv_file> <column1> [column2 ...]")

        csv_file = sys.argv[1]
        columns = [int(col) for col in sys.argv[2:]]

        # Perform the sum and print the results
        sums = sum_columns(csv_file, columns)
        print(f"Sums of specified columns {columns}: {sums}")

        # If everything worked correctly, exit with status 0
        sys.exit(0)
    except Exception as e:
        # If an error occurred, print an error message and exit with a non-zero status
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
