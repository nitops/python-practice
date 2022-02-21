# example to define single keys value pair
myfamily = {
    "name": "myra",
    'age': 2,
    "pob": None
}

print(myfamily['age'])

# list all keys of this list
print(myfamily.keys())

# list all values
print(myfamily.values())

# change value and then print
myfamily["age"] = 4
print(myfamily["age"])

# delete pob
del myfamily["pob"]
print(myfamily.keys())

# eammple to define multiple name value pair

myfamily1 = [
    {"name": "myra", 'age': 2, "pob": "ghaziabad"},
    {"name": "jia", 'age': 0.3, "pob": "ghaziabad"},
    {"name": "nitin", "age": 35, "pob": "faizabad"},
    {"name": "silky", "age": 26, "pob": "gorakhpur"}
]

# print age of jia
print(myfamily1[1]["age"])
