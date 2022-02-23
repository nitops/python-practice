""" getting list of Emails from csv and storing them as list"""

"""
In the above code we first import our csv library, which gives us the tools to parse our CSV file. 
We then create the empty list list_of_email_addresses which we’ll later populate with the email addresses from our CSV.
 Then we open the users.csv file with the temporary variable users_csv.
We pass the additional keyword argument newline='' to the file opening open() function 
so that we don’t accidentally mistake a line break in one of our data fields as a new row 
in our CSV (read more about this in the Python documentation).
After opening our new CSV file we use csv.DictReader(users_csv) which converts the lines of our CSV 
file to Python dictionaries which we can use access methods for. 
The keys of the dictionary are, by default, the entries in the first line of our CSV file. 
Since our CSV’s first line calls the third field in our CSV “Email“, we can use that as the key 
in each row of our DictReader.
When we iterate through the rows of our user_reader object, we access all of the rows in our CSV 
as dictionaries (except for the first row, which we used to label the keys of our dictionary). 
By accessing the 'Email' key of each of these rows we can grab the email address in that row and append 
it to our list_of_email_addresses.
"""
import csv

list_of_Emails = []
with open('users.csv', newline='') as users_csv:
    csv_content = csv.DictReader(users_csv)
    print(csv_content)  # Dict object
    print(csv_content.fieldnames)
    print(type(csv_content))
    for row in csv_content:
        # print(line['Email'])
        list_of_Emails.append(row['Email'])
    print(list_of_Emails)
