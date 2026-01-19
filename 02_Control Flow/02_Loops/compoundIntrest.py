#Compound Intrest Calculator

principle = 0
rate = 0
time = 0

while True:
    principle=float(input("Enter the Principle amount: "))
    if principle<=0:
        print("Principle amount can't be negative or equal to zero. ")
    else:
        break

while True:
    rate=float(input("Enter the Intrest rate: "))
    if principle<=0:
        print("Intrest rate can't be negative or equal to zero. ")
    else:
        break

while True:
    time=int(input("Enter the Time: "))
    if principle<=0:
        print("Time can't be negative or equal to zero. ")
    else:
        break


total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} year: ${total:.2f}.")