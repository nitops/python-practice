""" nested list example"""

names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 65]

""" If we wanted to create a list of lists that paired each name with a height, we could use the command zip. zip takes 
     two (or more) lists as inputs and returns an object that contains a list of pairs. Each pair contains 
   one element from each of the inputs. You won’t be able to see much about this object from just printing it:"""

names_and_heights = zip(names, heights)

print(names_and_heights)  # it will return the location of this object in memory.

""" To see the nested lists, you can convert the zip object to a list first: """
print(list(names_and_heights))
