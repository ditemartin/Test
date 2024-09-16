import streamlit as st

# Set up the page title and layout
st.set_page_config(page_title="Průvodce nástrojem pro ověřování shod", layout="wide")

# Adjust the page width using custom CSS
st.markdown(
    """
    <style>
    .main {
        max-width: 1400px;
        margin: 0 auto;
    }
    .button {
        display: inline-block;
        padding: 15px 25px;
        font-size: 20px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        color: white;
        background-color: #007BFF;
        border-radius: 5px;
        border: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Header
st.header("Průvodce nástrojem pro ověřování produktových párů")

# Přehled Section
st.subheader("Přehled")
st.write("""
Vítejte! Tento nástroj vám umožňuje ověřit, zda jsou produkty správně napárované.
""")

st.subheader("Jak na to?")
st.write("""
V některých případech to je velmi jednoduché a shoda/rozdíl jsou jasné na první pohled. Občas je třeba produkty prozkoumat detailně.
- Pokud si nejste jistí, použijte tlačítko **Přejít na web**, kde najdete další detaily.
- Pokud si ani po bližším prozkoumání nejste jistí, zda jsou produkty totožné, použijte tlačítko **Problematické**.
- Jestliže uděláte chybu, můžete se vrátit tlačítkem **Zpět**.
- Proces kontroly a důležité faktory se liší podle typu kontrolovaného zboží. U elektroniky sledujte jiné parametry než u koberců.
- Při kontrole často mohou pomoci produktové kódy od dodavatelů.
""")

st.subheader("Odměna")
st.write("""
Odměna je 150 Kč za 1.000 zkontrolovaných produktů.
""")

st.subheader("Přesnost")
st.write("""
Je nám jasné, že nikdo nedosáhne 100% přesnosti. Chceme ale vytvořit podmínky, které vám pomohou se k tomuto číslu co nejvíce přiblížit. Abychom zajistili co nejvyšší kvalitu služby, některé produktové páry budou vyhodnocovány několikrát. 
To nám umožní průběžně vyhodnocovat přesnost jednotlivých kontrolorů. Dlouhodobě by kontroloři měli dosahovat cca 98% přesnosti při vyhodnocování.
""")

# Add a blue button using HTML and CSS for external link
st.markdown(
    """
    <a href="https://www.example.com" target="_blank" class="button">Přejít do nástroje na kontrolu produktových párů</a>
    """,
    unsafe_allow_html=True
)

# Pravidla Section
st.header("Jak vyhodnotit nejednoznačné případy?")
st.write("""
Tato sekce obsahuje základní pravidla, která by měla být dodržována při ověřování shody produktů.
""")

# Helper function to create a rule section
def create_rule_section(rule_name, description, image_url1, image_url2):
    st.markdown(f"### {rule_name}")
    st.write(description)
    with st.expander(f"Příklad: {rule_name}"):
        col1, col2 = st.columns(2)
        with col1:
            st.image(image_url1, caption=f"{rule_name} - Obrázek 1")
        with col2:
            st.image(image_url2, caption=f"{rule_name} - Obrázek 2")

# Creating the rule sections
create_rule_section("Typ/vzhled", "Pokud produkt vypadá jinak (i když si jsou podobné), jde o jiný produkt.", "https://via.placeholder.com/300", "https://via.placeholder.com/300")
create_rule_section("Barva", "Produkty musí mít vždy stejnou barvu i vzor.", "https://via.placeholder.com/300", "https://via.placeholder.com/300")
create_rule_section("Velikost", "Produkty musí být stejně velké. Velikost je často dobrý ukazatel, pokud si podle obrázku nejste jistí, zda je produkt identický.", "https://via.placeholder.com/300", "https://via.placeholder.com/300")
create_rule_section("Počet v balení", "Některé produktové páry mohou být principiálně správně, ale v jednom obchodě se produkt prodává v jiném množství (např. židle vs. 4 židle).", "https://via.placeholder.com/300", "https://via.placeholder.com/300")
create_rule_section("Technické parametry", "Identicky vypadající produkty mohou mít jiné parametry: výkon, materiál, výdrž baterie, apod.", "https://via.placeholder.com/300", "https://via.placeholder.com/300")
