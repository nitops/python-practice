""" reading scores and creating dictionary from it. """

participants = {}  # creating empty dictionary
with open('scores.txt') as scores:
    for line in scores:
        score = line.strip().split(',')  # creating list out of each line of data
        print(score)
        name = score[0]
        score = score[1]
        participants[name] = score  # creating dictionary out of each name value pair
    print(participants)
