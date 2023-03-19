import unittest
import subprocess
from gradescope_utils.autograder_utils.decorators import weight, tags
from utility import get_code_file_name, get_function_info, get_test_cases, define_function_call
import ctypes
import os


class TestReturn(unittest.TestCase):
    code_file_name = get_code_file_name()

    test_cases = get_test_cases()

    function_info = get_function_info()

    def wrap_function(self, funcname, restype, argtypes):
        func = self.lib.__getattr__(funcname)

        func.restype = self.get_arg_type(restype)

        func.argtypes = [self.get_arg_type(arg) for arg in argtypes]

        return func

    def is_syntax_correct(self):
        cmd = f"gcc -c {self.code_file_name}"

        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True)

        return result.returncode == 0

    def generate_shared_code(self):
        cmd = f"gcc -shared -o test.so {self.code_file_name}"

        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True)

    def get_arg_type(self, arg):
        if arg == "<class 'ctypes.c_void_p'>":
            return ctypes.c_void_p

        elif arg == "<class 'ctypes._Pointer'> <class 'ctypes.c_int'>":
            return ctypes.POINTER(ctypes.c_int)

        elif arg == "<class 'ctypes.c_int'>":
            return ctypes.c_int

        elif arg == "<class 'list'>":
            return ctypes.POINTER(ctypes.c_int)

        else:
            return ctypes.c_int

    def get_arg_value(self, arg_type, arg):
        # print(arg_type," ", arg)
        if arg_type == ctypes.POINTER(ctypes.c_int):
            return ((ctypes.c_int)*len(arg))(*arg)

        else:
            return arg

    def setUp(self):
        # Define the function signature
        self.FuncType = ctypes.CFUNCTYPE(
            ctypes.c_void_p, *([ctypes.c_void_p] * ctypes.sizeof(ctypes.c_void_p)))

        self.lib = None

        self.function = None

        self.compilation_error = None

        if self.is_syntax_correct():

            self.compilation_error = False

            self.generate_shared_code()

            self.lib = ctypes.CDLL(os.path.abspath("./test.so"))

            if self.lib:
                self.function = self.wrap_function(
                    self.function_info['name'],
                    self.function_info['return_type'],
                    self.function_info['args_types'])

        else:
            self.compilation_error = True

    def return_value_test(self, expected_output, *args):
        message = "Correct !"

        if self.compilation_error:
            result = None
            message = "Compilation error"
            self.assert_(False, message)

        else:
            arg_values = []
            arg_type_classes = self.function_info['args_types']

            for i in range(len(arg_type_classes)):
                arg_type = self.get_arg_type(arg_type_classes[i])
                arg_values.append(self.get_arg_value(arg_type, args[i]))

            result = self.function(*arg_values)

            print(result)

            if result != expected_output:
                message = f"Test case failed. Input: {args}, Expected {expected_output}, but got {result}"

            self.assertTrue(result == expected_output, message)

    # Add weight decorator to each test case
    for i, test_case in enumerate(test_cases):
        locals()[f'test_{i+1}'] = weight(test_case['weight'])(lambda self,
                                                              test_case=test_case: define_function_call(self.return_value_test, test_case))
