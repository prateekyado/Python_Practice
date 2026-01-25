#Python reading files (.txt, .json, .csv)

file_path = "/Users/prateekyadav/Study/Data_Science/Python_Practice/06_File Handling & Error Handling/output.txt"

with open(file_path, "r") as file:
    content = file.read()
    print(content)
