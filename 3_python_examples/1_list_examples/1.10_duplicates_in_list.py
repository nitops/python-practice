""" Write a Python program to print set of duplicates in a list """

# Method 1
mylist = [1, 2, 3, 4, 4, 5, 5, 6, 1]

print(set([x for x in mylist if mylist.count(x) > 1]))

# Method 2 - same as above but in different manner

my_set = set(mylist)  # removing duplicate elements in the list

for i in my_set:
    if mylist.count(i) > 1:
        print(i)
