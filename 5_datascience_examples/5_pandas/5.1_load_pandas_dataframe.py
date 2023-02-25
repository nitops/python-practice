""""
Program to convert json file to pandas dataframe for easy representation
"""

import json
import pandas as pd

with open("../../1_basic_python/6_reading_writing_to_files/nested_json1.json") as f:
    file = json.load(f)

print(file["type"])

# print data frame

df = pd.read_json("supersquad.json")
print(df)

# The column ‘members’ would be much more convenient to work with in Pandas if each of the keys were actually
# individual columns.

print(df['members'].apply(pd.Series))

## combining 1st and 2nd df output

print(pd.concat([df['members'].apply(pd.Series), df.drop('members', axis=1)], axis=1))

"""
reference:
https://towardsdatascience.com/how-to-best-work-with-json-in-python-2c8989ff0390
https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html
same output as above can be acheived as follows:
record_path contains the column that we want parsed out.
meta is a list of columns we want to keep for the dataframe.
"""

with open("supersquad.json") as f1:
    file1 = json.load(f1)

print(pd.json_normalize(file1, record_path=['members'], meta=['squadName', 'homeTown', 'formed', 'secretBase', 'active']))