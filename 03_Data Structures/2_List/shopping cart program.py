#Shopping cart program

foods=[]
prices=[]
total=0

while True:
    food=input("Enter the food you want ( q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food} $: "))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total=total+price

print()
print(f"Your total bill is ${total:.2}. ")
print("----- THANK YOU -----")
