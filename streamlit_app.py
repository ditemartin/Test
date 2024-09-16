import streamlit as st

# Set up the page title and layout
st.set_page_config(page_title="Průvodce nástrojem pro ověřování shod", layout="wide", initial_sidebar_state="collapsed")

# Initialize session state for tab navigation
if 'active_tab' not in st.session_state:
    st.session_state['active_tab'] = 'Přehled'

# Sidebar with separate lines of text for navigation
with st.sidebar:
    st.markdown("# Menu")
    if st.button("Přehled"):
        st.session_state['active_tab'] = 'Přehled'
    if st.button("Pravidla"):
        st.session_state['active_tab'] = 'Pravidla'

# Helper function to create a collapsible rule section
def create_rule_section(rule_name, description):
    # Name and description above the collapsible section
    st.subheader(rule_name)
    st.write(description)
    with st.expander(f"Detail s příkladem: {rule_name}"):
        # Placeholder for images - replace with actual image URLs or paths if available
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://via.placeholder.com/300", caption=f"{rule_name} - Obrázek 1")
        with col2:
            st.image("https://via.placeholder.com/300", caption=f"{rule_name} - Obrázek 2")

# Show content based on active tab
if st.session_state['active_tab'] == 'Přehled':
    st.header("Průvodce nástrojem pro ověřování shod - Přehled")
    st.write("""
    Vítejte v nástroji pro ověřování shod! Tento nástroj vám umožňuje ověřit, zda jsou shody produktů mezi dvěma zdroji správné. Rozhraní zobrazuje informace o produktech vedle sebe pro snadné porovnání.

    - Použijte tlačítko **Správně** k potvrzení shody.
    - Použijte tlačítko **Nesprávně**, pokud produkty nesouhlasí.
    - Použijte tlačítko **Problematické**, pokud produkty potřebují další prošetření.
    - Tlačítko **Zpět** umožňuje vrátit poslední akci.

    Použijte navigaci v postranním panelu pro pohyb v průvodci a dozvědět se více o jednotlivých aspektech nástroje.
    """)

elif st.session_state['active_tab'] == 'Pravidla':
    st.header("Průvodce nástrojem pro ověřování shod - Pravidla")
    
    # Create rule sections
    create_rule_section("Barva", "Pravidlo pro shodu produktů podle barvy.")
    create_rule_section("Velikost", "Pravidlo pro shodu produktů podle velikosti.")
    create_rule_section("Počet v balení", "Pravidlo pro shodu produktů podle počtu v balení.")
    create_rule_section("Parametry", "Pravidlo pro shodu produktů podle konkrétních parametrů.")
    create_rule_section("Výrobce/původ", "Pravidlo pro shodu produktů podle výrobce nebo původu.")
