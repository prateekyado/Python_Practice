'''
*args   = allows you to pass multiple non-key argumnets
*kwargs = allows you to pass multiple keyword-raguments.
          * unpacking operator 
'''
#*args is type tuple.
def add(*args):  #here we can change *args with *nums, name is not important. "*" is.
    total = 0
    for arg in args:
        total += arg
    print(total)

#add(1,2,3,4,5,6)


#**kwargs s type dict

def print_add(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_add(town = "Sahawar",
          district = "Kasganj",
          State = "Uttar Pradesh",
          zip = "207245")

#
#
#