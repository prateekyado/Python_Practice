 #while loop = execute some code While some condition remain true.

name = input("Enter Your name: ")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")



age = int(input("Enter your age: "))
while age<0:
    print("age can't be negative!!")
    age = int(input("Enter your age: "))
print(f"You are {age} year old.")

num = int(input("Enter a number 1 - 10: "))

while num<1 or num>10:
    print(f"{num} is not valid.")
    num = int(input("Enter a number 1 - 10: "))
print(f"You have Entered {num}.")