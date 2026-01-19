#2D Collection (we can do the same with other collection like sets and tupple.)

fruits=["apple", "pinnapple", "banana", "coconut"]
vegetables = ["Patato", "Tamato", "Onion", "Chilly"]
masale = ["Mirch", "salt", "Garam Masala"]

groceries = [fruits, vegetables, masale]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()