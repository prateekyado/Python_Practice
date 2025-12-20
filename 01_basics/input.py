#here we will talk about input and output
#input()=A function that prompts the user to enter the data,
#        Return data will be string

name=input("Whats your name???")
age=input("Whats your age???")
print(type(age))
#<class 'str'>
age=int(age)
print(type(age))
#<class 'int'>
print(f"I'm {name}")