""" program demonstrating args and kwargs in functions"""


def myFun(arg1, *args, **kwargs):
    print("start of function,first argument is " + str(arg1) + "\n")
    for x in args:
        print(x)

    for key, value in kwargs.items():
        print("%s == %s" % (key, value))

    print("end of function")



print(myFun(2))
print(myFun(1))
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
myFun(1, first='Geeks', mid='for', last='Geeks')
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
