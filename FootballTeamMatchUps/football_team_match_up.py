team_name = input("Please enter a team name. ")
goals_1 = input("Goals scored in match #1: ")
goals_against_1 = input("Goals against in match #1: ")
goals_2 = input("Goals scored in match #2: ")
goals_against_2 = input("Goals against in match #2: ")
goals_3 = input("Goals scored in match #3: ")
goals_against_3 = input("Goals against in match #3: ")
goals_4 = input("Goals scored in match #4: ")
goals_against_4 = input("Goals against in match #4: ")
goals_5 = input("Goals scored in match #5: ")
goals_against_5 = input("Goals against in match #5: ")

wins = 0
draws = 0
losses = 0

if goals_1 > goals_against_1:
    wins += 1
elif goals_1 == goals_against_1:
    draws += 1
else:
    losses += 1

if goals_2 > goals_against_2:
    wins += 1
elif goals_2 == goals_against_2:
    draws += 1
else:
    losses += 1

if goals_3 > goals_against_3:
    wins += 1
elif goals_3 == goals_against_3:
    draws += 1
else:
    losses += 1

if goals_4 > goals_against_4:
    wins += 1
elif goals_4 == goals_against_4:
    draws += 1
else:
    losses += 1

if goals_5 > goals_against_5:
    wins += 1
elif goals_5 == goals_against_5:
    draws += 1
else:
    losses += 1

points = str((wins*3) + draws)


print(team_name)
print("Wins: " + str(wins))
print("Draws: " + str(draws))
print("Losses: " + str(losses))
print("Points: " + str(points))


