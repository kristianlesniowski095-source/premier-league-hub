teams = [
    {
    "team_name": "Arsenal",
    "games_played": 0,
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "goals_for": 0,
    "goals_against": 0,
    "points": 0
    },
    {
    "team_name": "Man City",
    "games_played": 0,
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "goals_for": 0,
    "goals_against": 0,
    "points": 0  
    },
    {
    "team_name": "Brighton",
    "games_played": 0,
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "goals_for": 0,
    "goals_against": 0,
    "points": 0   
    },
    {
    "team_name": "Chelsea",
    "games_played": 0,
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "goals_for": 0,
    "goals_against": 0,
    "points": 0 
    },
    {
    "team_name": "Liverpool",
    "games_played": 0,
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "goals_for": 0,
    "goals_against": 0,
    "points": 0 
    },
    {
    "team_name": "Everton",
    "games_played": 0,
      "wins": 0,
      "draws": 0,
      "losses": 0,
      "goals_for": 0,
      "goals_against": 0,
      "points": 0 
    },
    {
    "team_name": "Bournemouth",
    "games_played": 0,
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "goals_for": 0,
    "goals_against": 0,
    "points": 0 
    },
    {
    "team_name": "Brentford",
    "games_played": 0,
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "goals_for": 0,
    "goals_against": 0,
    "points": 0 
    },
    {
    "team_name": "Leeds",
    "games_played": 0,
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "goals_for": 0,
    "goals_against": 0,
    "points": 0
    },
    {
    "team_name": "Aston Villa",
    "games_played": 0,
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "goals_for": 0,
    "goals_against": 0,
    "points": 0 
    },
    {
    "team_name": "Tottenham",
    "games_played": 0,
    "wins": 0,
    "draws": 0,
    "losses": 0,
    "goals_for": 0,
    "goals_against": 0,
    "points": 0 
    },
    {
   "team_name": "Newcastle",
   "games_played": 0,
   "wins": 0,
   "draws": 0,
   "losses": 0,
   "goals_for": 0,
   "goals_against": 0,
   "points": 0 
    },
   {
   "team_name": "Hull City",
   "games_played": 0,
   "wins": 0,
   "draws": 0,
   "losses": 0,
   "goals_for": 0,
   "goals_against": 0,
   "points": 0 
   },
   {
   "team_name": "Ipswich Town",
   "games_played": 0,
   "wins": 0,
   "draws": 0,
   "losses": 0,
   "goals_for": 0,
   "goals_against": 0,
   "points": 0 
   },
   {
   "team_name": "Fulham",
   "games_played": 0,
   "wins": 0,
   "draws": 0,
   "losses": 0,
   "goals_for": 0,
   "goals_against": 0,
   "points": 0 
   },
   {
   "team_name": "Nottingham Forest",
   "games_played": 0,
   "wins": 0,
   "draws": 0,
   "losses": 0,
   "goals_for": 0,
   "goals_against": 0,
   "points": 0 
   },
   {
   "team_name": "Coventry City",
   "games_played": 0,
   "wins": 0,
   "draws": 0,
   "losses": 0,
   "goals_for": 0,
   "goals_against": 0,
   "points": 0 
   },
   {
   "team_name": "Man United",
   "games_played": 0,
   "wins": 0,
   "draws": 0,
   "losses": 0,
   "goals_for": 0,
   "goals_against": 0,
   "points": 0 
   },
   {
   "team_name": "Sunderland",
   "games_played": 0,
   "wins": 0,
   "draws": 0,
   "losses": 0,
   "goals_for": 0,
   "goals_against": 0,
   "points": 0 
   },
   {
   "team_name": "Crystal Palace",
   "games_played": 0,
   "wins": 0,
   "draws": 0,
   "losses": 0,
   "goals_for": 0,
   "goals_against": 0,
   "points": 0 
   }


]

matches = [
   {
   "home_team": "Arsenal",
   "away_team": "Chelsea",
   "home_goals": 2,
   "away_goals": 1
   },
   {
   "home_team": "Liverpool",
   "away_team": "Brighton",
   "home_goals": 0,
   "away_goals": 0
   },
   {
   "home_team": "Man City",
   "away_team": "Arsenal",
   "home_goals": 3,
   "away_goals": 1
   },
   {
   "home_team": "Arsenal",
   "away_team": "Brighton",
   "home_goals": 2,
   "away_goals": 0
   },
   {
   "home_team": "Everton",
   "away_team": "Newcastle",
   "home_goals": 2,
   "away_goals": 0
   }
]

for match in matches:
   for team in teams:
      if team["team_name"] == match["home_team"]:
         team["games_played"] += 1
         team["goals_for"] += match["home_goals"]
         team["goals_against"] += match["away_goals"]
         home_club = team
         
      if team["team_name"] == match["away_team"]:
         team["games_played"] += 1
         team["goals_for"] += match["away_goals"]
         team["goals_against"] += match["home_goals"]
         away_club = team

   if match["home_goals"] > match["away_goals"]:
      home_club["wins"] += 1
      home_club["points"] += 3
      away_club["losses"] += 1
   elif match["home_goals"] == match["away_goals"]:
      home_club["draws"] += 1
      home_club["points"] += 1
      away_club["draws"] += 1
      away_club["points"] += 1
   else:
      home_club["losses"] += 1
      away_club["wins"] += 1
      away_club["points"] +=3
         
def calculate_goal_difference(goals_for, goals_against):
   return goals_for - goals_against

for team in teams:
   team["goal_difference"] = calculate_goal_difference(team["goals_for"], team["goals_against"])

print("PREMIER LEAGUE TABLE")
print("2026/27 SEASON")

counter = 1

def get_points(team):
   return team["games_played"] > 0, team["points"], team["goal_difference"], team["goals_for"]
sorted_teams = sorted(teams, key=get_points, reverse=True)
print(f'{"Pos":>4} {"Team":<15} {"P":>4} {"W":>4} {"D":>4} {"L":>4} {"GF":>4} {"GA":>4} {"GD":>4} {"Pts":>4}')
for team in sorted_teams:
   print(f'{counter:>4} {team["team_name"]:<15} {team["games_played"]:>4} {team["wins"]:>4} {team["draws"]:>4} {team["losses"]:>4} {team["goals_for"]:>4} {team["goals_against"]:>4} {team["goal_difference"]:>+4} {team["points"]:>4}')
   counter = counter + 1
