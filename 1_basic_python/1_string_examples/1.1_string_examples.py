"""" This is a multiline comment"""
''' this is also comment'''
# this is a comment


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

print("My name is {0} and my age is {1}".format(name, age)) # 0 and 1 are index value

""" string concatenation"""
print("nitin " + "jain")

""" Inserting a string"""
print("Hello" + " " + "World")

""" type conversion in String - when we sum a integer with String it need to be type converted explicitly"""
print("My name is" + " Nitin" + " and I got " + str(15) + " years of experience")
x = 15
print("I got " + str(x) + " years of experience")
