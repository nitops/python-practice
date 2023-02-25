"""
Complete the program so that it calculates the length of the hypotenuse of a triangle (c), given two sides, a and b.
formula: length = surt(a^2 + b^2)
using round function, round-off the result to 1 decimal place
"""
import math
from math import sqrt


def diag_length(a: float, b: float) -> float:
    return math.sqrt((a * a) + (b * b))


length = float(input("Enter length of Triangle \n"))
width = float(input("Enter width of Traingle \n "))

print("length of the hypotenuse of a triangle")
print(round(diag_length(length, width), 1))
