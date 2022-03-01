""" Write a Python program to print a list in reverse """

li = [21, 1, 3, 4, 5, 6, 7, 8, 9, 19, 34, 36, 48, 50, 51]

li_copy = li.copy()  # note that if we just do l1_copy = li then both list will point to same memory address.
for i in li_copy:
    print(li[-1])
    li.remove(li[-1])

# Using build-in function
li_reverse = li_copy.copy()
li_reverse.reverse()
print(li_reverse)

# Method 3 using our own function:

my_list = [21, 1, 3, 4, 5, 6, 7, 8, 9, 19, 34, 36, 48, 50, 51]


def rev(mylist):
    return li[::-1]


print(rev(my_list))
