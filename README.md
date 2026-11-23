# Premier League Hub

A Python-based Premier League statistics project that retrieves football match results from an external API, processes the data and generates a league table.

## Current Version: v0.4

### Features

- 20-team Premier League database.
- Integration with the football-data.org API.
- Automatic retrieval of Premier League match data.
- Filtering of completed matches.
- Conversion of API responses into Python dictionaries.
- Automatic calculation of:
  - Games played
  - Wins, draws and losses
  - Goals scored and conceded
  - Goal difference
  - League points
- Automatic league table sorting based on:
  1. Points
  2. Goal difference
  3. Goals scored
- Validation checks for team records and goal totals.
- Formatted league table displayed in the terminal.
- API authentication using an environment variable.

### Technologies Used

- Python
- Requests
- python-dotenv
- football-data.org API
- Visual Studio Code
- Git and GitHub

### Project Structure

- `main.py` — Main programme containing API requests, data processing, calculations and league table generation.
- `README.md` — Project documentation.
- `requirements.txt` — External Python dependencies.
- `.gitignore` — Prevents sensitive and unnecessary files from being uploaded.
- `.env` — Stores the private API token locally (not uploaded to GitHub).

### Installation and Setup

1. Clone or download the repository.
2. Install the required dependencies:

   `py -m pip install -r requirements.txt`

3. Obtain an API token from [football-data.org](https://www.football-data.org/).
4. Create a `.env` file in the project folder.
5. Add your API token to the file using this format:

   `FOOTBALL_DATA_TOKEN=your_api_token_here`

6. Run the programme:

   `py main.py`

**Important:** Never upload your `.env` file or expose your API token publicly.

### Learning Objectives

This project is helping me develop my understanding of:

- Lists and dictionaries
- Loops and conditional statements
- Functions and return values
- Sorting and data processing
- APIs and HTTP requests
- JSON data handling
- Environment variables and API authentication
- Error handling and data validation
- Git and GitHub version control

### Planned Features

- Automatic retrieval of upcoming fixtures.
- Additional football statistics.
- Improved error handling.
- Further improvements to data processing and project structure.

### Development

This project is being developed incrementally, with each version introducing new functionality and improvements. Each milestone is documented and uploaded to GitHub.