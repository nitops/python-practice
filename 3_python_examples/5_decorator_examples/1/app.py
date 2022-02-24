""" An example on decorator which stores log output to file and also print to screen"""


def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as logfile:
            fname = function.__name__

            print(f"{fname} returned value {value}")
            logfile.write(f"{fname} returned value {value} \n")
        return value

    return wrapper


@logged
def add(x, y):
    return x + y


print(add(4, 6))  # this will call decorator which will add logs to logfile.txt and also print to screen
