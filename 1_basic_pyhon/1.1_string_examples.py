"""" This is a multiline comment"""

str1 = "nitin"

""" this will capitalize first letter """
print(str1.capitalize())

""" This will replace letter from str"""
print(str1.replace("i", "t"))  # this will replace i with t

""" This will return true if all characters are letters"""
print(str1.isalpha())

""" This will return true if all characters are digits"""
print(str1.isdigit())

""" Split method"""
print(str1.split())

str3 = "some,csv,file,is to,be,split".split(",")
print(str3)

""" String format"""
name = 'Myra'
age = 5

print("My name is {0} and my age is {1}".format(name, age))
