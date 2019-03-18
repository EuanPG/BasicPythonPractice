"""
Takes in scores of matches and prints out wins/draws/losses/points.
"""

__author__      = "Euan Geleziunas"
__email__       = "euanpgeleziunas@gmail.com"
__date__        = "15-11-2018"


team_name = input("Please enter a team name. ")
total_games = 1
wins = 0
draws = 0
losses = 0

while total_games <= 5:
    goals_scored = input("Goals scored in match #" + str(total_games) + ": ")
    goals_against = input("Goals scored in match #" + str(total_games) + ": ")
    if goals_scored > goals_against:
        wins = wins + 1
    elif goals_scored == goals_against:
        draws = draws + 1
    else:
        losses = losses + 1
    total_games = total_games + 1

total_points = (wins*3) + draws

print("\n")
print(team_name)
print("Wins: " + str(wins))
print("Draws: " + str(draws))
print("Losses: " + str(losses))
print("Points:" + str(total_points))
