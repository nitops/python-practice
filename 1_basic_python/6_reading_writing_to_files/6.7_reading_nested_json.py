import json
with open("purchase.json") as f:
    json_file = json.load(f)

print(json_file["item_id"])

with open("nested_json1.json") as f1:
    json_nested = json.load(f1)

print(json_nested["ppu"])

# reading id from topping
print(type(json_nested["topping"]))
print(json_nested["topping"][0]["id"])





