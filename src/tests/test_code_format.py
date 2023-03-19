import unittest
from gradescope_utils.autograder_utils.decorators import weight, tags
from utility import get_code_file_name

code_file = get_code_file_name()


class TestCodeContent(unittest.TestCase):
    @weight(2)
    @tags("sufficient_comments")
    def test_return_value1(self):
        """Every line of code has a comment"""
        # Read the program into a list
        with open(code_file, "r", encoding="utf8") as f_sub:
            code_lines = f_sub.readlines()

        # Set default values
        has_comments = False
        current_line = 0
        # previous_comment = False

        # Iterate through the code until either the end of code or
        # an uncommented line is found
        while current_line < len(code_lines):
            # print(f"line:{current_line}:", code_lines[current_line])

            # Only check code lines. Skip empty lines.
            if code_lines[current_line].strip().startswith("//"):
                has_comments = True

            # elif code_lines[current_line].strip().startswith("/*"):
            #     current_line += 1
            #     while (not code_lines[current_line].strip().endswith("*/")):
            #         current_line += 1
            #     previous_comment = True

            # elif not (
            #     code_lines[current_line].strip() == ""
            #     or code_lines[current_line].strip().endswith("\\")
            # ):
            #     if previous_comment:
            #         previous_comment = False
            #     else:
            #         has_comments = False

            current_line += 1

        # Give student feedback
        if has_comments:
            print("All lines commented.")
        else:
            # print("The line:\n")
            # print(code_lines[current_line - 1])
            print("Your code does not have any comments explaining what it does.")

        self.assertTrue(has_comments)
