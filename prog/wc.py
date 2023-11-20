import sys
import argparse

def count_words_chars_lines(input_text):
    lines = input_text.split('\n')
    num_lines = len([line for line in lines if line.strip()])  # Count non-empty lines
    num_words = sum(len(line.split()) for line in lines)
    num_chars = len(input_text)
    return num_chars, num_words, num_lines

def print_counts(filename, counts, flags):
    if 'l' in flags:
        print(f"{counts[2]:>8}", end=' ')
    if 'w' in flags:
        print(f"{counts[1]:>8}", end=' ')
    if 'c' in flags:
        print(f"{counts[0]:>8}", end=' ')
    print(filename)

def main():
    parser = argparse.ArgumentParser(description='Word, character, and line count utility')
    parser.add_argument('-l', action='store_true', help='Count lines')
    parser.add_argument('-w', action='store_true', help='Count words')
    parser.add_argument('-c', action='store_true', help='Count characters')
    parser.add_argument('files', nargs='*', help='Input files')
    
    args = parser.parse_args()

    if not any([args.l, args.w, args.c]):
        # If no flags provided, default to 'wc -lwc'
        args.l = args.w = args.c = True

    total_counts = [0, 0, 0]

    try:
        for filename in args.files:
            with open(filename, 'r') as file:
                input_text = file.read()
            counts = count_words_chars_lines(input_text)
            total_counts = [total + current for total, current in zip(total_counts, counts)]
            print_counts(filename, counts, [flag for flag, enabled in vars(args).items() if enabled])

        if args.files:
            if len(args.files) > 1:
                print_counts('total', total_counts, [flag for flag, enabled in vars(args).items() if enabled])

    except FileNotFoundError as e:
        print(f"wc: {e.filename}: No such file or directory")
        sys.exit(1) 

    except Exception as e:
        print(f"wc: An unexpected error occurred: {e}")
        sys.exit(1) 

    sys.exit(0) 

if __name__ == '__main__':
    main()
