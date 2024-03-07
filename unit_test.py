import subprocess
import unittest
import sys

class TestGrep(unittest.TestCase):

    def test_case_1(self):
        
        # Test case 1 (success case): search pattern, filename and option c
        print("------ Test case 1 (success) -------")
        print("# Test case 1 (success case): search pattern, filename and option c")


        search_pattern = "can"
        file_name      = "test.txt"


        my_script_command = f"python3 grep.py -c {search_pattern} {file_name}"
        script_output     = subprocess.check_output(my_script_command, shell=True, universal_newlines=True)
        

        print("\n"+'SCRIPT_COMMAND: ' + my_script_command)
        print("\n"+'SCRIPT_OUTPUT:' + "\n"+ script_output)


        actual_grep_command = f"grep -c {search_pattern} {file_name}"
        actual_grep_output  = ''


        try:
            actual_grep_output = subprocess.check_output(actual_grep_command, shell=True, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            actual_grep_output = e.output

        
        print("\n"+'ACTUAL_GREP_COMMAND: ' + actual_grep_command) 
        print("\n"+ 'ACTUAL_GREP_OUTPUT:' + "\n" + actual_grep_output)


        self.assertEqual(script_output, actual_grep_output)

    def test_case_2(self):
    
        # Test case 2 (failure case): search pattern - with extra char in grep.py input, filename and option c
        print("------ Test case 2 (failure) -------")
        print("# Test case 2 (failure case): search pattern - with extra char in grep.py input, filename and option c")


        search_pattern = "can"
        file_name      = "test.txt"


        my_script_command = f"python3 grep.py -c {search_pattern + 'c'} {file_name}"
        script_output     = subprocess.check_output(my_script_command, shell=True, universal_newlines=True)


        print("\n"+'SCRIPT_COMMAND: ' + my_script_command)
        print("\n"+'SCRIPT_OUTPUT:' + "\n" + script_output)


        actual_grep_command = f"grep -c {search_pattern} {file_name}"
        actual_grep_output  = ''


        try:
            actual_grep_output = subprocess.check_output(actual_grep_command, shell=True, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            actual_grep_output = e.output


        print("\n"+'ACTUAL_GREP_COMMAND: ' + actual_grep_command) 
        print("\n"+ 'ACTUAL_GREP_OUTPUT:' + "\n" + actual_grep_output)


        self.assertNotEqual(script_output, actual_grep_output)

    def test_case_3(self):

        # Test case 3 (success case): search pattern input, filename
        print("------ Test case 3 (success) -------")
        print("# Test case 3 (success case): search pattern input, filename")


        search_pattern = "random"
        file_name      = "test.txt"


        my_script_command = f"python3 grep.py {search_pattern} {file_name}"
        script_output     = subprocess.check_output(my_script_command, shell=True, universal_newlines=True)


        print("\n"+'SCRIPT_COMMAND: ' + my_script_command)
        print("\n"+'SCRIPT_OUTPUT:' + "\n" + script_output)


        actual_grep_command = f"grep {search_pattern} {file_name}"
        actual_grep_output  = ''


        try:
            actual_grep_output = subprocess.check_output(actual_grep_command, shell=True, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            actual_grep_output = e.output


        print("\n"+'ACTUAL_GREP_COMMAND: ' + actual_grep_command) 
        print("\n"+ 'ACTUAL_GREP_OUTPUT:' + "\n" +actual_grep_output)


        self.assertEqual(script_output, actual_grep_output)

    def test_case_4(self):

        # Test case 4 (success case): search pattern input, filename, option n h 
        print("------ Test case 4 (success) -------")
        print("# Test case 4 (success case): search pattern input, filename, option n h")


        search_pattern = "action"
        file_name      = "test.txt"


        my_script_command = f"python3 grep.py -nH {search_pattern} {file_name}"
        script_output     = subprocess.check_output(my_script_command, shell=True, universal_newlines=True)


        print("\n"+'SCRIPT_COMMAND: ' + my_script_command)
        print("\n"+'SCRIPT_OUTPUT:' + "\n" + script_output)


        actual_grep_command = f"grep -nH {search_pattern} {file_name}"
        actual_grep_output  = ''


        try:
            actual_grep_output = subprocess.check_output(actual_grep_command, shell=True, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            actual_grep_output = e.output


        print("\n"+'ACTUAL_GREP_COMMAND: ' + actual_grep_command) 
        print("\n"+ 'ACTUAL_GREP_OUTPUT:' + "\n" + actual_grep_output)


        self.assertEqual(script_output, actual_grep_output)

    def test_case_5(self):

        # Test case 5 (failure case): search pattern input, multiple files, option o n for grep.py and option o for actual grep
        print("------ Test case 4 (success) -------")
        print("# Test case 5 (failure case): search pattern input, multiple files, option o n i for grep.py and option o i for actual grep")


        search_pattern   = "STRING"
        file_name_1      = "test.txt"
        file_name_2      = "test.txt"


        my_script_command = f"python3 grep.py -noi {search_pattern} {file_name_1} {file_name_2}"
        script_output     = subprocess.check_output(my_script_command, shell=True, universal_newlines=True)


        print("\n"+'SCRIPT_COMMAND: ' + my_script_command)
        print("\n"+'SCRIPT_OUTPUT:' + "\n" +script_output)


        actual_grep_command = f"grep -oi {search_pattern} {file_name_1} {file_name_2}"
        actual_grep_output  = ''


        try:
            actual_grep_output = subprocess.check_output(actual_grep_command, shell=True, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            actual_grep_output = e.output


        print("\n"+'ACTUAL_GREP_COMMAND: ' + actual_grep_command)     
        print("\n"+ 'ACTUAL_GREP_OUTPUT:' + "\n" + actual_grep_output)


        self.assertNotEqual(script_output, actual_grep_output)

if __name__ == '__main__':
    sys.stdout = sys.__stdout__
    unittest.main()