
"""simple if demo"""
number = 5
if (number ==5):
    print ("Number is 5")
else:
    print("Number is not 5")

"""truthy value demo"""
if number:
 print("Number is defined and truthy")

""" and keyword can be used
    or keyword can be used in if """
a = 5
b = 10
if a ==5 and b ==10:
    print("true statement")

"""ternary if statement"""
print("bigger" if a > b  else "smaller")

"""not if demo"""
if a!= b:
    print("This will execute if a is not equal to b")