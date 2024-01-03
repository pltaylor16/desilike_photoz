import os
import re

# List of files to process
file_list = [
    'des-y3-6x2.ini',
    'des-y3_and_kids-1000.ini',
    'des-y3-maglim.ini',
    'des-y3-shear.ini',
    'kids-1000.ini',
    'des-y3.ini',               # Added 'des-y3.ini'
    'des-y3-maglim-values.ini',  # Added 'des-y3-maglim-values.ini'
    'des-y3-maglim-priors.ini',   # Added 'des-y3-maglim-priors.ini'
    'des-y3-maglim-values.ini']

# Process each file
for file_path in file_list:
    # Check if the file exists
    if os.path.isfile(file_path):
        # Read the file content
        with open(file_path, 'r') as file:
            file_content = file.read()

        # Perform replacements with regular expressions, case-insensitive
        file_content = re.sub(r'examples', r'${INI_FILE_DIR}', file_content, flags=re.IGNORECASE)
        file_content = re.sub(r'file\s*=\s*', r'file=${COSMOSIS_STD_DIR}/', file_content, flags=re.IGNORECASE)

        # Additional replacement
        file_content = file_content.replace('${COSMOSIS_STD_DIR}/%(2PT_FILE)s', '%(2PT_FILE)s')

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(file_content)

        print(f"Modified {file_path}")
    else:
        print(f"File not found: {file_path}")

