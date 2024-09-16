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
    st.subheader("Základní pravidla pro ověřování shod")
    st.write("""
    Tato sekce obsahuje základní pravidla, která by měla být dodržována při ověřování shody produktů.
    """)

    # Create rule sections
    create_rule_section("Barva", "Produkty musí mít vždy stejnou barvu i vzor.")
    create_rule_section("Velikost", "Produkty musí být stejně velké. Velikost je často velmi dobrý ukazatel, pokud si nejste jistí, zda je produkt identický.")
    create_rule_section("Počet v balení", "Některé produktové páry mohou být principiálně správně, ale v jednom z obchodů se produkt bude prodávat v jiném množství (např židle vs. 4 židle).")
    create_rule_section("Parametry", "Identicky vypadající produkty stále mohou mít jiné parametry.")
    create_rule_section("Výrobce/původ", "Pravidlo pro shodu produktů podle výrobce nebo původu.")
