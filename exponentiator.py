def exponentiate(x, y):
    '''general case for raising a given number to a specified exponent'''
    return x**y

def raise_to_the_fourth_power(x):
    '''get the 4th power of a given number'''
    return exponentiate(x, 4)

def square(x):
    '''get the square of a given number'''
    return exponentiate(x, 2)

def cube(x):
    '''get the cube of a given number'''
    return exponentiate(x, 3)

print(square(2))
print(cube(2))
print(raise_to_the_fourth_power(2))
