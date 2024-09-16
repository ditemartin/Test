import streamlit as st

# Set up the page title and layout
st.set_page_config(page_title="Průvodce nástrojem pro ověřování shod", layout="wide", initial_sidebar_state="expanded")  # Set sidebar to expanded

# Initialize session state for tab navigation
if 'active_tab' not in st.session_state:
    st.session_state['active_tab'] = 'Přehled'

# Sidebar with non-collapsible menu and normal text lines for navigation
with st.sidebar:
    st.markdown("# Menu")
    
    # Use markdown links to change the active tab
    if st.markdown("[Přehled](#)"):
        st.session_state['active_tab'] = 'Přehled'
    if st.markdown("[Pravidla](#)"):
        st.session_state['active_tab'] = 'Pravidla'

# Helper function to create a collapsible rule section with editable image URLs
def create_rule_section(rule_name, description, image_url1, image_url2):
    # Use a slightly smaller font size using custom HTML/CSS
    st.markdown(f"<h4 style='font-size:20px;'>{rule_name}</h4>", unsafe_allow_html=True)
    st.write(description)
    with st.expander(f"Příklad: {rule_name}"):
        # Images with provided URLs
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_url1, caption=f"{rule_name} - Obrázek 1")
        with col2:
            st.image(image_url2, caption=f"{rule_name} - Obrázek 2")

# Show content based on active tab
if st.session_state['active_tab'] == 'Přehled':
    st.header("Přehled")
    st.write("""
    Vítejte! Tento nástroj vám umožňuje ověřit, zda jsou produkty správně napárované.
    """)
    
    st.subheader("Jak na to?")
    
    st.write("""
    V některých případech to je velmi jednoduché a shoda/rozdíl jsou jasné na první pohled. Občas je třeba produkty prozkoumat detailně.
    - Pokud si nejste jistí, použijte tlačitko **Přejít na web**, kde najdete další detaily.
    - Pokud si ani po bližším prozkoumání nejste jistí, zda jsou produkty totožné, použijte tlačítko **Problematické**
    - Jestliže uděláte chybu, můžete se vrátit tlačítkem **Zpět**
    - Proces kontroly a důležité faktory, na které je třeba se soustředit, se budou lišit dle typu kontrolovaného zboží. U Elektroniky bude třeba sledovat jiné parametry než u koberců.
    - Při kontrole často mohou pomoci produktové kódy od dodavatelů
    """)

    st.subheader("Odměna")
    
    st.write("""
    Odměna je 150 Kč za 1.000 zkontrolovaných produktů.
    """)

    st.subheader("Přesnost")
    
    st.write("""
    Je nám jasné, že nikdo nedosáhne 100% přesnosti, chceme ale vytvořit podmínky, které vám pomohou se k tomuto číslu co nejvíce přiblížit. Abychom zajistili co nejvyšší možnou kvalitu služby pro naše zákazníky, některé produktové páry budou vyhodnocovány několikrát. 
    To nám navíc umožní průběžně vyhodnocovat přesnost jednotlivých kontrolorů. Pokud výsledky nebudou odpovídat očekávání, můžeme se pak zaměřit na konkrétní problémy. Dlouhodobě by kontroloři měli dosahovat cca 98% přesnosti při vyhodnocování.
    """)

elif st.session_state['active_tab'] == 'Pravidla':
    st.header("Jak vyhodnotit nejednoznačné případy?")
    st.write("""
    Tato sekce obsahuje základní pravidla, která by měla být dodržována při ověřování shody produktů.
    """)

    # Create rule sections with custom image URLs
    create_rule_section("Typ/vzhled", "Pokud produkt vypadá jinak (i když si jsou podobné), jde o jiný produkt.", "https://via.placeholder.com/300", "https://via.placeholder.com/300")
    create_rule_section("Barva", "Produkty musí mít vždy stejnou barvu i vzor.", "https://via.placeholder.com/300", "https://via.placeholder.com/300")
    create_rule_section("Velikost", "Produkty musí být stejně velké. Velikost je často velmi dobrý ukazatel, pokud si podle obrázku nejste jistí, zda je produkt identický.", "https://via.placeholder.com/300", "https://via.placeholder.com/300")
    create_rule_section("Počet v balení", "Některé produktové páry mohou být principiálně správně, ale v jednom z obchodů se produkt bude prodávat v jiném množství (např židle vs. 4 židle).", "https://via.placeholder.com/300", "https://via.placeholder.com/300")
    create_rule_section("Technické parametry", "Identicky vypadající produkty stále mohou mít jiné parametry. Výkon, materiál, výdrž baterie, apod.", "https://via.placeholder.com/300", "https://via.placeholder.com/300")
