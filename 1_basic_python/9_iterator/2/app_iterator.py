""" Below is a simple Python custom iterator that creates iterator type that iterates from 10 to a given limit.
For example, if the limit is 15, then it prints 10 11 12 13 14 15. And if the limit is 5, then it prints nothing."""


class Test:
    # Constructor
    def __init__(self, limit=0):
        self.limit = limit

    # Creates iterator object
    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self  # returns iterator object

    def __next__(self):
        x = self.x
        while x > self.limit:
            raise StopIteration

        self.x = x + 1
        return x


# Print numbers from 10 to 15
for i in Test(15):
    print(i)

# Prints Nothing
for j in Test(5):
    print(j)
