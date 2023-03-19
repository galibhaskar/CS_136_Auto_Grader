import json

with open('config.json', 'r') as f:
    config = json.load(f)

def get_code_file_name():
    # print(config)
    code_file = config['code_file']
    # print("code_file", code_file)
    return code_file