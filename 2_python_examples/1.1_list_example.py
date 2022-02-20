"""
Write a function named append_sum that has one parameter named lst.

The function should add the last two elements of lst together and append the result to lst. It should do this process

three times and then return lst.

For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8]. """


def add_lst(lst):
    i = 3
    while i > 0:
        lst.append(lst[-1] + lst[-2])
        i = i - 1

    return lst


print(add_lst([1, 1, 2]))
