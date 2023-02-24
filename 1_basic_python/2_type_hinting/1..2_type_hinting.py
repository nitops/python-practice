""" another program to demo type hinting """
greeting = "Hello, {}, you're {} years old"


def greet(user: str, age: int) -> str:
    return greeting.format(user, age)


name = input("Your name?")
age = int(input("How old are you?"))

print(greet(name, age))
