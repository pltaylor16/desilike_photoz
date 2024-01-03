import os
import re

# Get a list of files in the current directory ending with '-values.ini'
file_list = [filename for filename in os.listdir() if filename.endswith('-values.ini')]

# Function to modify a line by keeping only the middle number
def modify_line(line):
    numbers = re.findall(r'-?\d+\.\d+', line)  # Find all numbers in the line
    if len(numbers) == 3:
        return line.replace(numbers[0], '').replace(numbers[2], '')
    else:
        return line

# Process each file
for file_name in file_list:
    file_path = os.path.join(os.getcwd(), file_name)  # Full file path

    # Check if the file exists
    if os.path.isfile(file_path):
        # Read the file content
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Modify each line and store the modified content
        modified_content = [modify_line(line) for line in lines]

        # Write the modified content back to the file with the same name
        with open(file_path, 'w') as file:
            file.writelines(modified_content)

        print(f"Modified {file_name}")
    else:
        print(f"File not found: {file_name}")
'''
import os
import re

# Get a list of files in the current directory ending with '-values.ini'
file_list = [filename for filename in os.listdir() if filename.endswith('-values.ini')]

# Function to modify a line by keeping only the middle number
def modify_line(line):
    # Find all numbers in the line, including scientific notation
    numbers = re.findall(r'-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?', line)

    if len(numbers) == 3:
        return line.replace(numbers[0], '').replace(numbers[2], '')
    else:
        return line

# Process each file
for file_name in file_list:
    file_path = os.path.join(os.getcwd(), file_name)  # Full file path

    # Check if the file exists
    if os.path.isfile(file_path):
        # Read the file content
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Modify each line and store the modified content
        modified_content = [modify_line(line) for line in lines]

        # Write the modified content back to the file with the same name
        with open(file_path, 'w') as file:
            file.writelines(modified_content)

        print(f"Modified {file_name}")
    else:
        print(f"File not found: {file_name}")
'''
