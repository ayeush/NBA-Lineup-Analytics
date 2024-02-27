import pandas as pd
import streamlit as st
import plotly.express as px

# import data
df = pd.read_csv('NBALineup2024.csv')

# Title for app
st.set_page_config(layout="wide")
st.title('Compare Any Two Lineups')

st.write("-------------------")

team1 = st.selectbox(
     'Choose Your First Team:',
     df['team'].unique())

# Collect team data
# Get the first team data
df_team1 = df[df['team'] == team1].reset_index(drop=True)  
df_team1['players_list'] = df_team1['players_list'].str.replace("[", '')
df_team1['players_list'] = df_team1['players_list'].str.replace(r"[\"\' \[\]]", '')
df_team1['players_list'] = df_team1['players_list'].str.replace("]", '')
df_team1['players_list'] = df_team1['players_list'].str.replace("'", '')
df_team1['players_list'] = df_team1['players_list'].str.split(', ')
duplicate_roster1 = df_team1['players_list'].apply(pd.Series).stack()
cleaned_duplicate1 = duplicate_roster1.str.strip()
roster1 = cleaned_duplicate1.unique()

# Get first lineup
players1 = st.multiselect(
     'Select your first lineup',
     roster1,
     roster1[0:5])

# Select second team
team2 = st.selectbox(
     'Choose Your Second Team:',
     df['team'].unique())
# Get the second team data
if (team1 != team2):
    df_team2 = df[df['team'] == team2].reset_index(drop=True)
    df_team2['players_list'] = df_team2['players_list'].str.replace("[", '')
    df_team2['players_list'] = df_team2['players_list'].str.replace(r"[\"\' \[\]]", '')
    df_team2['players_list'] = df_team2['players_list'].str.replace("]", '')
    df_team2['players_list'] = df_team2['players_list'].str.replace("'", '')
    df_team2['players_list'] = df_team2['players_list'].str.split(', ')
    duplicate_roster2 = df_team2['players_list'].apply(pd.Series).stack()
    cleaned_duplicate2 = duplicate_roster2.str.strip()
    roster2 = cleaned_duplicate2.unique()
else:
    df_team2 = df_team1
    roster2 = roster1

players2 = st.multiselect(
     'Select your second lineup',
     roster2,
     roster2[0:5])


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

st.write("-------------------")

# Check if 5 players are selected
if (len(players1) != 5) or (len(players2) != 5):
    st.error("Make sure you are picking 5 players for both lineups")
else:
    # Find the right line ups
    df_lineup1 = df_team1[df_team1['players_list'].apply(lambda x: set(x) == set(players1))]
    df_lineup2 = df_team2[df_team2['players_list'].apply(lambda x: set(x) == set(players2))]
    empty_df_check = False
    if not df_lineup1.empty:
        if not df_lineup2.empty:
            empty_df_check = True
    if empty_df_check:
        df_important1 = df_lineup1[stats_mapping[selected_stat]]
        #st.dataframe(df_important1)
        df_important2 = df_lineup2[stats_mapping[selected_stat]]
        #st.dataframe(df_important2)

        col1, col2 = st.columns(2)

        with col1: 
            st.write("First Lineup ", selected_stat, " ", df_important1.values[0])
            fig_min = px.histogram(df_team1, x=stats_mapping[selected_stat])
            fig_min.add_vline(x=df_important1.values[0], line_color='red')
            st.plotly_chart(fig_min, use_container_width=True)

        with col2: 
            st.write("Second Lineup ", selected_stat, " ", df_important2.values[0])
            fig_2 = px.histogram(df_team2, x=stats_mapping[selected_stat])
            fig_2.add_vline(x=df_important2.values[0], line_color='red')
            st.plotly_chart(fig_2, use_container_width=True)
    else:
        if df_lineup1.empty:
            st.error("No lineup found matching the selected players for your first lineup")
        if df_lineup2.empty:
            st.error("No lineup found matching the selected players for your second lineup")  
