"""demo for break in loop
we will break loop as soon we find myra"""

names = ["nitin", "sachin", "silky", "devansh", "myra", "jia", "saloni", "saanvi", "gunni"]

for name in names:
    print("Currently testing " + name)
    if name == "myra":
        print("Found her! " + name)
        break

# demo for continue in loop
# we will skip loop as soon we find myra

for name in names:
    print("Currently testing " + name)
    if name == "jia":
        continue
        print("Found her! " + name)
