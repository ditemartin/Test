import streamlit as st

# Set up the page title and layout
st.set_page_config(page_title="Průvodce při ověřování produktových párů", layout="wide")

# Adjust the page width using custom CSS
st.markdown(
    """
    <style>
    .main {
        max-width: 1200px;
        margin: 0 auto;
    }
    .custom-button {
        background-color: #d0e7ff;  /* Slightly blue background */
        color: black;  /* Black text */
        font-size: 18px;  /* Slightly larger font size */
        padding: 10px 20px;
        border: 2px solid #609BFF;  /* Border to resemble the original button shape */
        border-radius: 18px;
        text-align: center;
        display: inline-block;
        cursor: pointer;
    }
    .custom-button:hover {
        background-color: #b0d4ff;  /* Slightly darker blue on hover */
    }
    /* Reduce padding and margins in the Streamlit container */
    .stImage {
        padding: 0;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Header
st.header("Průvodce nástrojem pro ověřování shod")

# Přehled Section
st.subheader("Jak na to?")
st.write("""
V některých případech to je velmi jednoduché a shoda/rozdíl jsou jasné na první pohled. Občas je třeba produkty prozkoumat detailně.
- Pokud si nejste jistí, použijte tlačítko **Přejít na web**, kde najdete další detaily.
- Pokud si ani po bližším prozkoumání nejste jistí, zda jsou produkty totožné, použijte tlačítko **Problematické**.
- Jestliže uděláte chybu, můžete se vrátit tlačítkem **Zpět**.
- Proces kontroly a důležité faktory se liší podle typu kontrolovaného zboží. U elektroniky sledujte jiné parametry než u koberců.
- Při kontrole často mohou pomoci produktové kódy od dodavatelů.

Odměna je 150 Kč za 1.000 zkontrolovaných produktů.
""")

st.subheader("Přesnost")
st.write("""
Je nám jasné, že nikdo nedosáhne 100% přesnosti. Chceme ale vytvořit podmínky, které vám pomohou se k tomuto číslu co nejvíce přiblížit. Abychom zajistili co nejvyšší kvalitu služby, některé produktové páry budou vyhodnocovány několikrát. 
To nám umožní průběžně vyhodnocovat přesnost jednotlivých kontrolorů. Dlouhodobě by kontroloři měli dosahovat cca 98% přesnosti při vyhodnocování.
""")

# Add a slightly blue button using custom styling
st.markdown(
    """
    <a href="https://www.example.com" target="_blank">
        <div class="custom-button">Přejít do nástroje na kontrolu produktových párů</div>
    </a>
    """,
    unsafe_allow_html=True
)

# Pravidla Section
st.header("Jak vyhodnotit nejednoznačné případy?")
st.write("""
Tato sekce obsahuje základní pravidla, která by měla být dodržována při ověřování shody produktů.
""")

# Helper function to create a rule section with a single image
def create_rule_section(rule_name, description, image_path, width=800):
    st.markdown(f"### {rule_name}")
    st.write(description)
    with st.expander(f"Příklad: {rule_name}"):
        st.image(image_path, caption=f"{rule_name} - Obrázek", use_column_width=True)

# Creating the rule sections with the correct image paths
create_rule_section("Typ/vzhled", "Pokud produkt vypadá jinak (i když si jsou podobné), jde o jiný produkt.", "images/Type.png")
create_rule_section("Barva", "Produkty musí mít vždy stejnou barvu i vzor.", "images/Color.jpg")
create_rule_section("Velikost", "Produkty musí být stejně velké. Velikost je často dobrý ukazatel, pokud si podle obrázku nejste jistí, zda je produkt identický.", "images/Size.jpg")
create_rule_section("Počet v balení", "Některé produktové páry mohou být logicky správně, ale v každém obchodě se produkt prodává v jiném množství (např. židle vs. 4 židle).", "https://via.placeholder.com/300")
create_rule_section("Technické parametry", "Identicky vypadající produkty mohou mít jiné parametry: výkon, materiál, výdrž baterie, apod.", "images/Parameter.jpg")
