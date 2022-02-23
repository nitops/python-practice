""" joining values in list """

lis = ["mango", "papaya", "apple", "guvava"]

for i in lis:
    print(i + " and ", end="")

print("\n")
# above joining list can also be achieved as follows:

a = " and ".join(lis)
print(a)
