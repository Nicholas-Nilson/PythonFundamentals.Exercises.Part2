def greet(name):
    """prints a greeting to the given name"""
    print("hey there " + name)


def name_input():
    '''asks user for their name, for nefarious purposes later'''
    user_name = input("what's your name?\n")
    # greet(user_name)
    return user_name


print("greet docstring: " + greet.__doc__)
print("name input docstring: " + name_input.__doc__)

# name_input()
greet(name_input())