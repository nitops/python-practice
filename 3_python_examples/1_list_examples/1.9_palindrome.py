""" Write a Python program to check whether a string is a Palindrome or not """

""" Palindrome a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run."""


def get_len(nam):
    x = len(nam)
    return x


def get_looptime(x):
    if x % 2 == 0:
        loop_time = int(x / 2)
    else:
        loop_time = int((x - 1) / 2)

    return loop_time


def is_palindrome(my_str):
    i = 0
    x = get_len(my_str)
    loop = get_looptime(x)
    while loop > 0:
        loop -= 1
        if name[i] != name[x - i - 1]:  # checking 1st and last letter, 2nd and 2nd
            # last and so on until half of String is traversed
            return False
            break
        else:
            return True


print("Enter String to check if it's a Palindrome or not \n")

name = input()
if is_palindrome(name):
    print(name + " is palindrome")
else:
    print(name + " is not palindrome")

# Method 2: using build-in function

rev = ''.join(reversed(name))
if rev == name:
    print(name + " is palindrome")

else:
    print(name + " is not palindrome")
