import unittest
from gradescope_utils.autograder_utils.decorators import weight
from gradescope_utils.autograder_utils.files import check_submitted_files

from utility import get_code_file_name
import subprocess

code_file = get_code_file_name()

class TestSyntax(unittest.TestCase):
    @weight(2)
    def test_syntax(self):
        cmd = f"gcc -c {code_file}"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)