#Python read

import csv

file_path = "/Users/prateekyadav/Study/Data_Science/Python_Practice/06_File Handling & Error Handling/students.csv"

with open(file_path, "r") as file:
    content = csv.reader(file)
    for line in content:
        #print(line)
        print(line[0], " - ",line[1], " - ",line[2])