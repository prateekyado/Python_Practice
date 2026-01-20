#**kwargs always follow the *args.

def print_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('town')}, {kwargs.get('district')}")
    print(f"{kwargs.get('State')}, {kwargs.get('zip')}")


print_label("Mr.", "Prateek", "Yadav",
            town = "Sahawar",
            district = "Kasganj",
            State = "Uttar Pradesh",
            zip = "207245")
