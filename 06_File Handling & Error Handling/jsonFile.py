#.json file is made up of key-value pair.

import json
employee = {"name" : "Rahul",
            "age" : 30,
            "job" : "cook"}

file_path = "employee.json"

with open(file_path, "w") as file:
    json.dump(employee, file, indent= 4)
