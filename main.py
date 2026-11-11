teams = [
    {
    "team_name": "Arsenal",
    "games_played": 9,
    "wins": 8,
    "draws": 0,
    "losses": 1,
    "goals_for": 14,
    "goals_against": 5,
    "points": 24
    },
    {
    "team_name": "Man City",
    "games_played": 9,
    "wins": 7,
    "draws": 0,
    "losses": 2,
    "goals_for": 20,
    "goals_against": 10,
    "points": 21  
    },
    {
    "team_name": "Brighton",
    "games_played": 9,
    "wins": 6,
    "draws": 1,
    "losses": 2,
    "goals_for": 24,
    "goals_against": 7,
    "points": 19   
    },
    {
    "team_name": "Chelsea",
    "games_played": 9,
    "wins": 5,
    "draws": 1,
    "losses": 3,
    "goals_for": 19,
    "goals_against": 15,
    "points": 16 
    },
    {
    "team_name": "Liverpool",
    "games_played": 9,
    "wins": 4,
    "draws": 3,
    "losses": 2,
    "goals_for": 11,
    "goals_against": 9,
    "points": 15 
    }
    ]
 
def calculate_goal_difference(goals_for, goals_against):
   return goals_for - goals_against

for team in teams:
   team["goal_difference"] = calculate_goal_difference(team["goals_for"], team["goals_against"])

print("PREMIER LEAGUE TABLE")
print("2026/27 SEASON")

counter = 1

def get_points(team):
   return team["points"], team["goal_difference"], team["goals_for"]
sorted_teams = sorted(teams, key=get_points, reverse=True)
print(f'{"Pos":>4} {"Team":<15} {"P":>4} {"W":>4} {"D":>4} {"L":>4} {"GF":>4} {"GA":>4} {"GD":>4} {"Pts":>4}')
for team in sorted_teams:
   print(f'{counter:>4} {team["team_name"]:<15} {team["games_played"]:>4} {team["wins"]:>4} {team["draws"]:>4} {team["losses"]:>4} {team["goals_for"]:>4} {team["goals_against"]:>4} {team["goal_difference"]:>+4} {team["points"]:>4}')
   counter = counter + 1
