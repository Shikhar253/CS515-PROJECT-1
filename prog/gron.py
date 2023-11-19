import json
import sys
import argparse

def flatten_json(json_obj, base_object, parent_key='', separator='.'):
    flattened = {}
    for key, value in json_obj.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened.update(flatten_json(value, base_object, new_key, separator=separator))
        else:
            flattened[new_key] = value
    return flattened

def print_flattened_json(flattened_json, base_object):
    for key, value in flattened_json.items():
        print(f"{base_object}{key} = {json.dumps(value)};")

def main():
    parser = argparse.ArgumentParser(description='JSON flattening utility')
    parser.add_argument('--obj', type=str, default='json', help='Base object name')
    parser.add_argument('files', nargs='*', help='Input files')
    
    args = parser.parse_args()

    try:
        for filename in args.files:
            with open(filename, 'r') as file:
                json_data = json.load(file)
                flattened_json = flatten_json(json_data, args.obj)
                print_flattened_json(flattened_json, args.obj)

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON in file {filename}: {e}")
        sys.exit(1)  # Exit with non-zero status for JSON parsing error

    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
        sys.exit(1)  # Exit with non-zero status for file not found error

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit with non-zero status for unexpected error

    sys.exit(0)  # Exit with status 0 for successful execution

if __name__ == '__main__':
    main()
