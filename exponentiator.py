def exponentiate(x, y):   #how else can this be printed w/o using print() in the function itself?
    '''general case for raising a given number to a specified exponent'''
    print(x**y)

def raise_to_the_fourth_power(x):
    '''get the 4th power of a given number'''
    exponentiate(x, 4)

def square(x):
    '''get the square of a given number'''
    exponentiate(x, 2)

def cube(x):
    '''get the cube of a given number'''
    exponentiate(x, 3)

square(2)
cube(2)
raise_to_the_fourth_power(2)
