# Python file detection.
import os 

file_path = "/Users/prateekyadav/Study/Data_Science/Python_Practice/06_File Handling & Error Handling/test.txt"

if os.path.exists(file_path):
    print(f"location '{file_path} does exist. '")

    if os.path.isfile(file_path):
        print("This is a file")
    elif os.path.isdir(file_path):
        print("This is a directory.")
else:
    print("The location doesn't exist.") 