import streamlit as st

# Set up the page title and layout
st.set_page_config(page_title="Match Verification Tool User Guide", layout="wide")

# Collapsible sidebar
with st.sidebar:
    st.markdown("# Menu")
    tab = st.selectbox(
        "Navigate to:",
        ["Overview", "Rules"]
    )

# Content based on the selected tab
if tab == "Overview":
    st.header("Match Verification Tool - Overview")
    st.write("
    Welcome to the Match Verification Tool! This tool allows you to verify if the product matches between two sources are correct. The interface displays product information side by side to facilitate easy comparison.
    
    - Use the **Correct** button to confirm a match.
    - Use the **Incorrect** button if the products do not match.
    - Use the **Problematic** button if the products need further investigation.
    - The **Undo** button allows you to revert the last action.
    
    Please navigate through this guide using the sidebar to learn more about the different aspects of the tool.
    ")

elif tab == "Rules":
    st.header("Match Verification Tool - Rules")
    st.write("""
    This section covers the rules for verifying product matches in the tool.
    
    ### Rules:
    - **Correct**: If the products match exactly (all attributes such as Name, Price, EAN, Size, and Color match), select the green checkmark.
    - **Incorrect**: If there is a discrepancy in any attribute (e.g., Name or Price), select the red cross.
    - **Problematic**: If the products require further investigation (e.g., insufficient information), select the yellow button.
    - **Undo**: To
