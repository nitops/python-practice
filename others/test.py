# ends the output with a <space>
# print("Welcome to", end=' ')
# print("GeeksforGeeks", end=' ')


def make_printer(msg):
    def printer():
        print(msg)

    return printer


printer = make_printer('Foo!')
printer()
print(make_printer("Jain").__name__)
