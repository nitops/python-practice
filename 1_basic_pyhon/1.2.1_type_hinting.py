""" basic program to demonstrate type hinting"""


# define function to add two numbers
def add_numbers(a1: int, b1: int) -> float:
    return a1 + b1


# when adding two integers then no error
a = 10
b = 20
print(add_numbers(a, b))

""" when adding integer with float , although it wont give an error but when hovering mouse to y which is float 
    our editor would automatically complain """
x = 4
y = 10.0
print(add_numbers(x, y))


