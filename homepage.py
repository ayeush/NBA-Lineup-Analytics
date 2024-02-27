import streamlit as st
from streamlit import multipage
import importlib.util
import sys

app = multipage.App()

# Function to dynamically import a module
def import_module_from_path(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

# Dynamically import your pages
page_names_to_paths = {
    "Pick Your Own Lineup": "pages/2_📊_Pick_Your_Own_Lineup.py",
    "Best Stat Lineup": "pages/3_📊_Find_The_Best_Lineup_For_a_Stat.py",
    "Compare Lineups": "pages/4_📊_Compare_Different_Lineups.py",
}

for page_name, path in page_names_to_paths.items():
    module = import_module_from_path(page_name, path)
    app.add_page(page_name, module.app)

if __name__ == "__main__":
    app.run()


# Title for app
st.set_page_config(page_title='NBA Lineup Analysis Tool', page_icon='Hello', layout='wide')
st.title('NBA Lineup Analysis Tool')
st.sidebar.success("Select Page Above")