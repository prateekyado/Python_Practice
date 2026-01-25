'''
Docstring for 06_File Handling & Error Handling.list writing
'''

employees = ["Harsh", "Divya", "Prateek"]
file_path = "output.txt"

try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + " ")
except FileExistsError:
    print("File already exis")