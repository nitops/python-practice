import json

with open("purchase.json") as purchase_json:
  purchase_data = json.load(purchase_json)
print(type(purchase_data))

print(purchase_data["user"])
# Prints 'ellen_greg'


