"""
This program will add two different list into third empty list

"""

list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 10, 11, 12]
list3 = []
list4 = []
# perform addition using append

list3.append(list1)
list3.append(list2)
print(list3)

# perform addition using extend
list4.extend(list1)
list4.extend(list2)

print(list4)


"""
output:
[[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
"""