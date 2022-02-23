""" reading from file and writing to file """

with open('file1_sample.txt') as file:
    content = file.read()  # this reads all lines
print(content)

""" reading first  from file """
with open('file1_sample.txt') as file1:
    content1 = file1.readline()  # this only reads first line
print(content1)

""" reading line by line  from file """
with open('file1_sample.txt') as file1:
    content1 = file1.readlines()  # this reads each line and stores them in a list, extra '\n' is added to list
print(content1)


""" iterating through lines"""

""" reading line by line  from file """
with open('file1_sample.txt') as file1:
    content1 = file1.readlines()
    for line in content1:
        print(line)    # this reads each line and stores iteratively from list
