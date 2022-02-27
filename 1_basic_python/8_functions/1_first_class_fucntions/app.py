""" python program to demonstrate first class functions"""


def square(x):
    return x * x


f = square(5) # calling the function
f1 = square   # assigning function as variable or object to f1

print(f)
print(f1)
print(f1(5))  # using function object to execute function by passing argument to it.


