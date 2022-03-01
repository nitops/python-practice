""" write a python program to sort numbers in a list in ascending order
"""

# demo with built-in function

list_a = [24, 55, 78, 64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]

list_a.sort(reverse=False)
for i in list_a:
    print(i)

# demo without built-in function

list_b = [24, 55, 78, 64, 25, 12, 22, 11, 1, 2, 44, 3, 122, 23, 34]
new_list = []
while list_b:
    min_value = list_b[0]  # arbitrary number in list
    for x in list_b:
        if x < min_value:
            min_value = x
    new_list.append(min_value)
    list_b.remove(min_value)

print(new_list)
