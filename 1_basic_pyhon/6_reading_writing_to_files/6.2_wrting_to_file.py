""" writing content to file """

file_name = "file2_write_sample.txt"

with open(file_name, 'w') as file:  # with 'w' we ensure file is open in write mode
    file.write("This is first line \n")
    file.close()

"""" appending more contents to file """

with open(file_name, 'a') as file:  # with 'a' we ensure file is open in append mode
    file.write("...adding more content to existing file")
    file.close()
