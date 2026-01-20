'''
keyword arguments = an argument precede by an identifier
                    helps with readability
                    order of arguments doesn't matter
'''
#postional argummets follows keywords arguments

def hello(greetings, title, name, last):
    print(f"{greetings} {title}{name} {last}")

hello("Good Morning", "Mr.", "Prateek", "Yadav") #this is the example of the positional arguments
hello("Good Morning", name="Prateek", last="Yadav", title="Mr.") #here the order doesn't matter 
