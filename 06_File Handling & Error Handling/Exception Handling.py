# exception = An event that interrupts the flow of a program.
#             (ZeroDivision, TypeError, ValueError)
#             1. try, 2. except, 3. finally

try:
    number = int(input("Enter a number: "))
    print(1/number)

except ZeroDivisionError: #it only prints when you divide by zero
    print("You Can't divide by Zero, IDIOT!!")
except ValueError: #it only prints when you put wrong values
    print("Enter only Numbers.")

except Exception: #it includes all the exception
    print("Something went wrong! ")
finally:  #it always print, wheather there is any error or not.
    print("Do something cleanup here ")