#default argumnets: A default value for certain parameters
#                   default is used when that arguments is omitted
#                   make your functions more flexible, reduces # of arguments
#                   1. positional, 2. Default, 3. keyword, 4. arbitary

def net_price(list_price, discount = 0, tax=0.05):
    return list_price * (1 - discount) * ( 1+ tax)

print(net_price(500))
print(net_price(500,0.1))

