import os
from dotenv import load_dotenv 
load_dotenv()
import requests

api_token = os.getenv("FOOTBALL_DATA_TOKEN")

if api_token == None :
 print("API token not found")
 exit()
else:
   print("API token loaded successfully")

url = ("https://api.football-data.org/v4/competitions/PL/matches?season=2026")

headers = {
   "X-Auth-Token": api_token

}

try:
   response = requests.get(url, timeout=3 ,headers=headers)
except:
   print("API connection failed")
   exit()
if response.status_code == 200:
   print("Working")
else:
   print("Not Working")
   exit()
data = response.json()
finished_matches = []

for match in data["matches"]:
   if match["status"] == "FINISHED":
    finished_matches.append(match)

match_data = []
for match in finished_matches:
   ended_game = {"home_team":match["homeTeam"]["shortName"], "away_team":match["awayTeam"]["shortName"], "home_goals":match["score"]["fullTime"]["home"], "away_goals":match["score"]["fullTime"]["away"]}
   match_data.append(ended_game)

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
    "team_name": "Brighton Hove",
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
    "team_name": "Leeds United",
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
   "team_name": "Nottingham",
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

matches = match_data


for match in matches:
   home_club = None
   away_club = None
   for team in teams:
      if team["team_name"] == match["home_team"]:
         home_club = team
         
      if team["team_name"] == match["away_team"]:
         away_club = team

   if (home_club == None
   or away_club == None):
    print("None")
    continue

   home_club["games_played"] += 1
   home_club["goals_for"] += match["home_goals"]
   home_club["goals_against"] += match["away_goals"]

   away_club["games_played"] += 1
   away_club["goals_for"] += match["away_goals"]
   away_club["goals_against"] += match["home_goals"]


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

sum_of_goals = 0
for team in teams:
      sum_of_goals += team["goals_for"]

sum_of_conceded = 0
for team in teams:
      sum_of_conceded += team["goals_against"]

if sum_of_goals == sum_of_conceded:
   print("Goal totals validated successfully")
else:
   print("Error")

all_teams_valid = True
for team in teams:
   if team["wins"] + team["draws"] + team["losses"] == team["games_played"]:
      pass
   else:
    all_teams_valid = False

if all_teams_valid == True:
   print("Works good")
else:
   print("Not working")
     
         
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
