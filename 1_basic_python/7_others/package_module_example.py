import random

while True:
    num = input("Enter any number between 1_first_class_fucntions to 6, press 'q' to quit \n")
    num1 = random.randint(1, 6)
    if num == num1:
        print("you won the gamble")
    elif num == 'q':
        print("Quitting .....")
        break
    elif int(num) > 6:
        print("Enter number between 1_first_class_fucntions and 6 only ")
    else:
        print("try again")
