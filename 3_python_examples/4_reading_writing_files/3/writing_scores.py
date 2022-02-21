# writing data to file and looping until you want to quit

f = open("scores1.txt", "w")

while True:

    participant = input("Enter name of participant \n")
    if participant == 'quit':
        print("Quitting .....")
        break
    score = input("Enter score for " + participant + "\n")
    f.write(participant + "," + score + "\n")

f.close()
