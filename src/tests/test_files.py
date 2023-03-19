import unittest
from gradescope_utils.autograder_utils.decorators import weight
from gradescope_utils.autograder_utils.files import check_submitted_files

from utility import get_code_file_name

code_file = get_code_file_name()

# print("test files:", code_file)


class TestFiles(unittest.TestCase):
    @weight(2)
    def test_submitted_files(self):
        f"Submitted file is named {code_file}"
        # Check submitted files
        missing_files = check_submitted_files([code_file])
        # print(missing_files)
        for path in missing_files:
            print("Missing {0}".format(path))
        self.assertEqual(len(missing_files), 0, "Missing some required files!")
        print("All required files submitted!")
