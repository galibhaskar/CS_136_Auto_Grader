import unittest
import subprocess
from gradescope_utils.autograder_utils.decorators import weight, tags
from utility import get_code_file_name
import ctypes
import os

code_file_name = get_code_file_name()


class TestReturn(unittest.TestCase):
    test_cases = [
        {"input": [1, 2, 3], "expected_output": 6, "weight": 2},
        {"input": [-1, -2, -3], "expected_output": -6, "weight": 2},
        {"input": [0, 0, 0, 0, 0, 0], "expected_output": 0, "weight": 2},
        {"input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "expected_output": 55, "weight": 2},
        {"input": [-10, 5, 3, -2, 0, 8, -7],
            "expected_output": -3, "weight": 2},
        {"input": [], "expected_output": 0, "weight": 2}
    ]

    lib = None

    def compile_code(self):
        cmd = f"gcc -shared -o test.so {code_file_name}"
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True)
        

    def setUp(self):
        self.compile_code()

        self.lib = ctypes.CDLL(os.path.abspath("./test.so"))

        if self.lib:
            self.lib.calculateTotalInArray.argtypes = [
                ctypes.POINTER(ctypes.c_int), ctypes.c_int]

            self.lib.calculateTotalInArray.restype = ctypes.c_int

    def return_value_test(self, input_arr, expected_output):
        result = self.lib.calculateTotalInArray(
            (ctypes.c_int * len(input_arr))(*input_arr), len(input_arr))

        self.assertTrue(result == expected_output,
                        f"Test case failed. Input: {input_arr}, Expected {expected_output}, but got {result}")

    # Add weight decorator to each test case
    for i, test_case in enumerate(test_cases):
        locals()[f'test_{i+1}'] = weight(test_case['weight'])(lambda self,
                                                              test_case=test_case: self.return_value_test(test_case['input'], test_case['expected_output']))
