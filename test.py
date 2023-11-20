import os
import subprocess

class TestResult:
    Pass = "PASS"
    Fail = "FAIL"
    OutputMismatch = "TestResult.OutputMismatch"

def run_test(program, test_name, input_filename, expected_output_filename):
    input_file_path = os.path.join('test', f'{program}.{test_name}.in')
    expected_output_file_path = os.path.join('test', f'{program}.{test_name}.out')
    arg_expected_output_file_path = os.path.join('test', f'{program}.{test_name}.arg.out')
    
    if(program=="gron"):
        program_path = os.path.join('prog', 'gron.py')
        process = subprocess.Popen([program_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        process = subprocess.Popen([program], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    with open(input_file_path, 'r') as input_file:
        program_output, _ = process.communicate(input=input_file.read().encode('utf-8'))

    # Check if the program output matches the expected output
    with open(expected_output_file_path, 'r') as expected_output_file:
        expected_output = expected_output_file.read()

    if program_output.decode('utf-8') == expected_output:
        # First test passed, now run with a command-line argument
        process = subprocess.Popen([program, input_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        program_output_arg, _ = process.communicate()

        # Check if the argument output matches the expected argument output
        with open(arg_expected_output_file_path, 'r') as arg_expected_output_file:
            expected_output_arg = arg_expected_output_file.read()

        if program_output_arg.decode('utf-8') == expected_output_arg:
            return TestResult.Pass
        else:
            print(f"{TestResult.Fail}: {program} {test_name} (Argument Output Mismatch)")
            print("      expected argument output:")
            print(expected_output_arg)
            print("\n           got:")
            print(program_output_arg.decode('utf-8'))
            return TestResult.OutputMismatch
    else:
        print(f"{TestResult.Fail}: {program} {test_name} (Output Mismatch)")
        print("      expected:")
        print(expected_output)
        print("\n           got:")
        print(program_output.decode('utf-8'))
        return TestResult.OutputMismatch

def main():
    programs = ["wc","csv_sum"]
    test_results = {TestResult.Pass: 0, TestResult.Fail: 0, TestResult.OutputMismatch: 0}
    for program in programs:
        test_files = [f for f in os.listdir('test') if f.startswith(f"{program}.") and f.endswith('.in')]
        for test_file in test_files:
            test_name = test_file[len(program) + 1:-3]  # Extract the test name
            result = run_test(program, test_name, test_file, f"{program}.{test_name}.out")

            if result == TestResult.Fail or result == TestResult.OutputMismatch:
                test_results[result] += 1

    # Print summary of test results
    for result, count in test_results.items():
        print(f"{result}: {count}")

    total_tests = sum(test_results.values())
    print(f"total: {total_tests}")

    # Exit with a non-zero status if any test failed
    if test_results[TestResult.Fail] > 0 or test_results[TestResult.OutputMismatch] > 0:
        exit(1)

if __name__ == '__main__':
    main()
