file = open("countries.txt", "r")

countries = []

for line in file:
    line = line.strip()  # to remove   whitespaces and save back to line.
    countries.append(line)
file.close()  # file need to be closed once you open it. // old way to deal with files

print(countries)

print(len(countries))

# based on user input countries would be displayed.
user_input = input("Enter First letter for Country you wish to filter \n")
user_input = user_input.capitalize()
print(user_input)
for country in countries:
    if country.startswith(user_input):
        print(country)
