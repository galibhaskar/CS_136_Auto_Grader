import zipfile
import os

# List the files you want to include in the zip
file_list = ['tests/test_code_format.py', 'tests/test_files.py',
             'tests/test_return.py', 'tests/test_syntax.py',
             'config.json', 'convert_to_ascii.py', "utility.py",
             "requirements.txt", "run_autograder", "run_tests.py", "setup.sh"]

# Set the name of the zip file you want to create

version = "1.1.0"

zip_path = f"../builds/autograder_v{version}.zip"

# Create a new zip file
with zipfile.ZipFile(zip_path, 'w') as my_zip:

    # Loop through the file list and add each file to the zip
    for file in file_list:
        my_zip.write(file)

# Check if the zip file was created successfully
if os.path.exists(zip_path):
    print(f"{zip_path} created successfully!")
else:
    print("Error: Zip file not created.")
