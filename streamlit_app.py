import streamlit as st

# Set up the page title and layout
st.set_page_config(page_title="Match Verification Tool User Guide", layout="wide", initial_sidebar_state="collapsed")

# Sidebar with individual buttons for navigation
with st.sidebar:
    st.markdown("# Menu")
    overview_button = st.button("Overview")
    rules_button = st.button("Rules")

# Helper function to create a collapsible rule section
def create_rule_section(rule_name, description):
    with st.expander(f"{rule_name} (Click to expand)"):
        st.write(description)
        # Placeholder for images - replace with actual image URLs or paths if available
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://via.placeholder.com/300", caption=f"{rule_name} - Image 1")
        with col2:
            st.image("https://via.placeholder.com/300", caption=f"{rule_name} - Image 2")

# Show content based on button click
if overview_button:
    st.header("Match Verification Tool - Overview")
    st.write("""
Welcome to the Match Verification Tool! This tool allows you to verify if the product matches between two sources are correct. The interface displays product information side by side to facilitate easy comparison.

- Use the **Correct** button to confirm a match.
- Use the **Incorrect** button if the products do not match.
- Use the **Problematic** button if the products need further investigation.
- The **Undo** button allows you to revert the last action.

Please navigate through this guide using the sidebar to learn more about the different aspects of the tool.
    """)

elif rules_button:
    st.header("Match Verification Tool - Rules")
    
    # Create rule sections
    create_rule_section("Barva", "Rule for matching products based on color.")
    create_rule_section("Velikost", "Rule for matching products based on size.")
    create_rule_section("Počet v balení", "Rule for matching products based on the quantity in the package.")
    create_rule_section("Parametry", "Rule for matching products based on specific parameters.")
    create_rule_section("Výrobce/původ", "Rule for matching products based on manufacturer/origin.")

