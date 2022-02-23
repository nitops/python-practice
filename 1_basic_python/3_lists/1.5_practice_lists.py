inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table',
             'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow',
             'pillow']

# inventory is a list of items that are in the warehouse for Bob’s Furniture. How many items are in the warehouse?

print(len(inventory))

# count how many times 'twin bed' appears in inventory

print(inventory.count('twin bed'))

# printed new list of sorted inventory.Note this does not impact original list

inventory_sorted = sorted(inventory)
print(inventory)
print(inventory_sorted)

# sort inventory, note that this will sort existent inventory list itself but its return is None
inventory_sort = inventory.sort()
print(inventory_sort)
print(inventory)
