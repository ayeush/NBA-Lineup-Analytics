import pandas as pd
import streamlit as st
import plotly.express as px

# import data
df = pd.read_csv('NBALineup2024.csv')

# Title for app
st.set_page_config(layout="wide")
st.title('Maximum Statistic Lineup')


team = st.selectbox(
     'Choose Your Team:',
     df['team'].unique())

# Get just the selected team 
df_team = df[df['team'] == team].reset_index(drop=True)
df_team['players_list'] = df_team['players_list'].str.replace(r"[\"\' \[\]]", '')
df_team['players_list'] = df_team['players_list'].str.replace("[", '')
df_team['players_list'] = df_team['players_list'].str.replace("]", '')
df_team['players_list'] = df_team['players_list'].str.replace("'", '')
df_team['players_list'] = df_team['players_list'].str.split(',')


# Select statistic
stats_mapping = {
    "Games Played": "GP",
    "Wins": "W",
    "Losses": "L",
    "Win Percentage": "W_PCT",
    "Minutes": "MIN",
    "Field Goals Made": "FGM",
    "Field Goals Attempted": "FGA",
    "Field Goal Percentage": "FG_PCT",
    "Three Point Field Goals Made": "FG3M",
    "Three Point Field Goals Attempted": "FG3A",
    "Three Point Field Goal Percentage": "FG3_PCT",
    "Free Throws Made": "FTM",
    "Free Throws Attempted": "FTA",
    "Free Throw Percentage": "FT_PCT",
    "Offensive Rebounds": "OREB",
    "Defensive Rebounds": "DREB",
    "Rebounds": "REB",
    "Assists": "AST",
    "Turnovers": "TOV",
    "Steals": "STL",
    "Blocks": "BLK",
    "Blocks Against": "BLKA",
    "Personal Fouls": "PF",
    "Personal Fouls Drawn": "PFD",
    "Points": "PTS",
    "Plus Minus": "PLUS_MINUS",
    "Games Played Rank": "GP_RANK",
    "Wins Rank": "W_RANK",
    "Losses Rank": "L_RANK",
    "Win Percentage Rank": "W_PCT_RANK",
    "Minutes Rank": "MIN_RANK",
    "Field Goals Made Rank": "FGM_RANK",
    "Field Goals Attempted Rank": "FGA_RANK",
    "Field Goal Percentage Rank": "FG_PCT_RANK",
    "Three Point Field Goals Made Rank": "FG3M_RANK",
    "Three Point Field Goals Attempted Rank": "FG3A_RANK",
    "Three Point Field Goal Percentage Rank": "FG3_PCT_RANK",
    "Free Throws Made Rank": "FTM_RANK",
    "Free Throws Attempted Rank": "FTA_RANK",
    "Free Throw Percentage Rank": "FT_PCT_RANK",
    "Offensive Rebounds Rank": "OREB_RANK",
    "Defensive Rebounds Rank": "DREB_RANK",
    "Rebounds Rank": "REB_RANK",
    "Assists Rank": "AST_RANK",
    "Turnovers Rank": "TOV_RANK",
    "Steals Rank": "STL_RANK",
    "Blocks Rank": "BLK_RANK",
    "Blocks Against Rank": "BLKA_RANK",
    "Personal Fouls Rank": "PF_RANK",
    "Personal Fouls Drawn Rank": "PFD_RANK",
    "Points Rank": "PTS_RANK",
    "Plus Minus Rank": "PLUS_MINUS_RANK"
}

selected_stat = st.selectbox(
    'Select a Statistic:',
    list(stats_mapping.keys()))

# Find the row with the max value of the selected statistic
max_stat_row = df_team.loc[df_team[stats_mapping[selected_stat]].idxmax()]

# Extract players from the max stat row
max_stat_players = max_stat_row['players_list']

max_stat_players_string = ''
for individual in max_stat_players:
    max_stat_players_string += individual
    max_stat_players_string += ", "
max_stat_players_string = max_stat_players_string[:-2]
    
# Display the players from the lineup with the highest selected stat
st.write(f"Players from the lineup with the highest {selected_stat}:")
st.write(max_stat_players_string)

players = max_stat_players

if len(players) == 5:
  # Find the right lineup
  df_lineup = df_team[df_team['players_list'].apply(lambda x: set(x) == set(players))]
  if not df_lineup.empty:
    df_important = df_lineup[['GP','W','L','W_PCT','MIN','FGM','FGA','FG_PCT','FG3M','FG3A','FG3_PCT','FTM','FTA','FT_PCT','OREB','DREB','REB','AST','TOV','STL','BLK','BLKA','PF','PFD','PTS','PLUS_MINUS','GP_RANK','W_RANK','L_RANK','W_PCT_RANK','MIN_RANK','FGM_RANK','FGA_RANK','FG_PCT_RANK','FG3M_RANK','FG3A_RANK','FG3_PCT_RANK','FTM_RANK','FTA_RANK','FT_PCT_RANK','OREB_RANK','DREB_RANK',"REB_RANK",'AST_RANK','TOV_RANK','STL_RANK','BLK_RANK','BLKA_RANK','PF_RANK','PFD_RANK','PTS_RANK','PLUS_MINUS_RANK']]
    columns_to_format = df_important.columns
    for col in columns_to_format:
      df_important[col] = df_important[col].round(2).astype(str).str.rstrip('0').str.rstrip('.')

    st.dataframe(df_important)

    fig_main = px.histogram(df_team, x=stats_mapping[selected_stat])
    fig_main.add_vline(x=df_important[stats_mapping[selected_stat]].values[0], line_color='red')
    st.plotly_chart(fig_main, use_container_width=True)

  else:
    st.error("No lineup found matching the selected players.")
else:
    st.error("Make sure you are picking 5 players")