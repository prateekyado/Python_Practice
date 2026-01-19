#   list = [] ordered and changeable. Duplicates are ok


fruits = ["apple", "orange", "banana", "coconut"]
print(fruits) 
print(fruits[0]) #give the index element
print(fruits[::-1]) #reverse the list
print(fruits[::2]) #give the alternative element
fruits[3] = "pinneapple" #change the element at index 0;
fruits.append("Grapes") #this will add new element at the end of the list.
fruits.remove("apple")#this will remove the given element from the list
fruits.insert(0,"Guava") # this will add the element at the given index not not replace it
fruits.sort() #this will sort the list in alphabetical order
fruits.reverse() #this will reverse the list
fruits.index("apple") #this will tell the index of the element
fruits.clear() # this will make the list empty




#iterate over all the item in list
for fruit in fruits:
    print(fruit)

'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''