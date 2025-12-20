#here we will make an calcultor;
operator=input("Enetr the opertor (+ - * /): ")
num1= int(input("Enter the 1st num: "))
num2=int(input("Enter the second num: "))

if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1-num2
elif operator == "*":
    result = num1*num2
elif operator == "/":
    result = num1/num2
else:
    result="Error"

print(result)