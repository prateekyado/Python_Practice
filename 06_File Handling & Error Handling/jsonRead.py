#Python read

import json

file_path = "/Users/prateekyadav/Study/Data_Science/Python_Practice/06_File Handling & Error Handling/employee.json"

with open(file_path, "r") as file:
    content = json.load(file)
    print(content)