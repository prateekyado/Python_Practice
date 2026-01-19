#concession stand program

menu ={"pizza": 250,
       "samosa": 15,
       "bhelpuri": 10,
       "popcorn": 100,
       "tikki": 20}

cart=[]
total=0

print("------- MENU -------")

for key, value in menu.items():
    print(f"{key:10}: ${value}")

print("--------------------")

while True:
    food = input("Enter the Food (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)

print()

print("------- YOUR ORDER -------")

for food in cart:
    print(food)
print()

print(f"Your Total order is ${total}. ")
print()
print("--------------------------")
