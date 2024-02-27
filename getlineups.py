# libraries
from nba_api.stats.endpoints import teamdashlineups
from nba_api.stats.static import teams
import pandas as pd
import numpy as np
import logging

# Configure logging
logging.basicConfig(filename='getlineups.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Logging is configured. Starting script execution.")

# get teams
nba_teams = teams.get_teams()
team_dict = {}
for i in nba_teams:
  name = i['full_name']
  id = i['id']
  team_dict[name] = id
logging.info(f"Successfully fetched {len(nba_teams)} NBA teams.")


# Function to get the lineups given a team id for the 2023-24 season
def get_lineups(team_id_i):

    lineup = teamdashlineups.TeamDashLineups(
      date_from_nullable = "",
      date_to_nullable = "",
      game_id_nullable = "",
      game_segment_nullable = "",
      group_quantity = 5,
      last_n_games = 0,
      league_id_nullable = "00",
      location_nullable = "",
      measure_type_detailed_defense = "Base",
      month = 0,
      opponent_team_id = 0,
      outcome_nullable = "",
      pace_adjust = "N",
      plus_minus = "N",
      po_round_nullable = "",
      per_mode_detailed = "Totals",
      period = 0,
      rank = "N",
      season = "2023-24",
      season_segment_nullable = "",
      season_type_all_star = "Regular Season",
      shot_clock_range_nullable = "",
      team_id = team_id_i,
      vs_conference_nullable = "",
      vs_division_nullable = ""
      )
    
    df = lineup.get_data_frames() # get the data 
    all_lineups = df[1] # grab all possible lineups
    #print(all_lineups.to_string())
    
    return all_lineups

league_lineup_df = pd.DataFrame()  # Change variable name to avoid conflict
for i in team_dict:
    team_id_i = team_dict[i]
    team_lineup = get_lineups(team_id_i)
    team_lineup['team'] = i  # adding team name column
    team_lineup['team_id'] = team_id_i  # adding team id column
    league_lineup_df = pd.concat([league_lineup_df, team_lineup], ignore_index=True)

league_lineup_df['players_list'] = league_lineup_df['GROUP_NAME'].str.split(' - ')
league_lineup = league_lineup_df.sort_values(by='team')
logging.info(f"Writing league lineup data to NBALineup2024.csv. Total lineups: {len(league_lineup_df)}")
league_lineup.to_csv('NBALineup2024.csv')
logging.info("Script execution completed successfully. The data is now available in NBALineup2024.csv.")
