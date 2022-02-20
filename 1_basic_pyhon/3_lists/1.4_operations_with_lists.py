""" different operation with lists"""

# find length

fruits = ["Mango", "Apple", "Banana", "Pears"]
print(len(fruits))

# find element at given location
print(fruits[1])

""" count elements in list """

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake',
         'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
print(votes.count("Jake"))

""" sorting list """

names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
names.sort()

print(names)

names.sort(reverse=True)
print(names)
