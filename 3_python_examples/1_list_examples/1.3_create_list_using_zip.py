"""
Use zip to create a new variable called names_and_dogs_names that combines names and dogs_names into a zip object.

Make sure to run the code for this step before proceeding to the next instruction!

2.
Create a new variable named list_of_names_and_dogs_names by calling list() on names_and_dogs_names. Print this new variable .
"""

names = ["name1", "name2", "name3"]
dog_names = ["dog1", "dog2", "dog3"]
names_and_dogs_names = zip(names, dog_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)
