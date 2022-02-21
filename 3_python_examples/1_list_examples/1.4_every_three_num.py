"""
Create a function called every_three_nums that has one parameter named start.

The function should return a list of every third number between start and 100 (inclusive).

 For example, every_three_nums(91) should return the list [91, 94, 97, 100].

 If start is greater than 100, the function should return an empty list.
"""


def every_three_nums(start):
    lst = []
    if start > 100:
        return lst
    while start <= 100:
        lst.append(start)
        start += 3
    return lst


print(every_three_nums(91))
