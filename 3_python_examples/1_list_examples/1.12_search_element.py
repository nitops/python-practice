""" Given an array arr[] of n elements, write a Python function to search a given element x in arr[] """
""" this is also called linear search """

l = [1, 2, 3, 4, 4, 5, 5, 6, 1]


def search(arr, x):
    for i in range(len(arr)):
        if x == arr[i]:
            return True
    return False


if search(l, 10):
    print("element found in Array")
else:
    print("element not found in Array")
