'''
Docstring for 06_File Handling & Error Handling.csvFile
'''

import csv

students = [["Name ", "Roll NO ", "Age "],
            ["Harsh ", 187, 21],
            ["Divya ", 221, 20],
            ["Ayush ", 223, 19]]

file_path = "students.csv"

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in students:
        writer.writerow(row)