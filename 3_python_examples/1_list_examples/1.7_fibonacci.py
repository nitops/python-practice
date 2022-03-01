""" Write a Python program to print Fibonacci Series """

print("Enter upper range of the Fibonacci Series \n")
upper = int(input())

a = 0
b = 1
c = a + b
final_list = [0]

for i in range(2, upper):
    if c <= upper:
        final_list.append(c)
        c = a + b
        a = b
        b = c

    else:
        break
print(final_list)

# Method 2
final_list2 = []


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(0, 12):
    if fib(i) <= upper:
        final_list2.append(fib(i))

print(final_list2)
