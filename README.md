# NBA Lineup Analysis Tool

## Description
This is a Streamlit web application designed to analyze NBA lineups. It allows users to pick their own lineup, find the best lineup based on a selected statistic, and compare different lineups. The tool provides visualizations and key statistics for better analysis.

## Features
- **Pick Your Own Lineup**:
  - Users can select their preferred team and choose 5 players to form their lineup.
  - The tool displays relevant statistics for the selected lineup, including minutes played, plus/minus, field goal percentage, and three-point percentage.

- **Find The Best Lineup For a Statistic**:
  - Users can choose a statistic of interest (e.g., points, rebounds, assists) and the tool identifies the lineup with the highest value for that statistic.
  - The lineup with the maximum value for the selected statistic is displayed along with its corresponding statistics.

- **Compare Different Lineups**:
  - Users can compare two different lineups from different teams.
  - After selecting two lineups, users can choose a statistic to compare, and the tool visualizes the distribution of that statistic for both lineups, highlighting the values of each lineup.

## File Structure
homepage.py # Main file to run the application
└─── pages/
└─── 2_📊_Pick_Your_Own_Lineup.py # Page to pick your own lineup
└─── 3_📊_Find_The_Best_Lineup_For_a_Stat.py # Page to find the best lineup for a statistic
└─── 4_📊_Compare_Different_Lineups.py # Page to compare different lineups
requirements.txt # List of required Python packages with versions
NBALineup2024.csv # CSV file containing NBA lineup data (not provided in the structure)
