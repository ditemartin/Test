import streamlit as st

# Set up the page title and layout
st.set_page_config(page_title="Match Verification Tool User Guide", layout="wide", initial_sidebar_state="collapsed")

# Sidebar with text for navigation
with st.sidebar:
    st.markdown("# Menu")
    if st.session_state.get("active_tab") == "Rules":
        st.markdown("**Rules**")
        st.markdown("[Overview](#)", unsafe_allow_html=True)
    else:
        st.markdown("**Overview**")
        st.markdown("[Rules](#)", unsafe_allow_html=True)

# Set the active tab based on the user's selection
if st.session_state.get("active_tab") == "Rules" or "Rules" in st.session_state.get("active_tab", "Overview"):
    active_tab = "Rules"
else:
    active	tab["defiant_panelconfiguration",
