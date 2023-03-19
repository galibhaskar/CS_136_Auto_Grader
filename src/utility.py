import json
import ctypes

with open('config.json', 'r') as f:
    config = json.load(f)

def get_code_file_name():
    return config['code_file']

def get_test_cases():
    return config['test_cases']

def get_function_info():
    return config['function']

def define_function_call(function, test_case):
    return function(test_case['expected_output'], test_case['input'], len(test_case['input']))