import streamlit as st

# Title for app
st.set_page_config(page_title='NBA Lineup Analysis Tool', page_icon='🏀', layout='wide')
st.title('NBA Lineup Analysis Tool')

# Introduction
st.write("This Streamlit web application is designed to analyze NBA lineups. It provides various features for lineup selection, analysis, and comparison.")
st.markdown("---")

# Features
st.header("Features:")
st.write("1. **Pick Your Own Lineup:**")
st.write("   - Select your preferred team and choose 5 players.")
st.write("   - View relevant statistics for the selected lineup.")
st.write("2. **Find The Best Lineup For a Statistic:**")
st.write("   - Choose a statistic of interest (e.g., points, rebounds).")
st.write("   - Identify the lineup with the highest value for the selected statistic.")
st.write("3. **Compare Different Lineups:**")
st.write("   - Compare two lineups from different teams.")
st.write("   - Visualize the distribution of a selected statistic for both lineups.")
st.markdown("---")

# Additional Information or Tips
st.header("Tips:")
st.write("- Explore and analyze NBA lineups effortlessly using the sidebar.")
st.write("- Have fun experimenting with different player combinations!")
