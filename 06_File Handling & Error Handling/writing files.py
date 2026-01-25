#Python writing files (.txt, .json, .csv)
# "w": is for write, it can also overwrite the data 
# "x": it'll write the file, if it doesn't exist.
# "a" : it'll append the data
text_data = "I like Aloo ke parathe."

file_path = "/Users/prateekyadav/Study/Data_Science/Python_Practice/06_File Handling & Error Handling/output.txt"

try:
    with open(file_path,"x") as file: # this will automatically close your file.
        file.write(text_data)
        print(f"txt file '{file_path}' was created. ")
except FileExistsError:
    print("File already exist.")