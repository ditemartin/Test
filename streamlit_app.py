import streamlit as st

st.set_page_config(page_title="Průvodce pro ověřování produktových párů", layout="wide")

# Adjust the page width using custom CSS
st.markdown(
    """
    <style>
    .main {
        max-width: 1200px;
        margin: 0 auto;
    }
    .custom-button {
        background-color: #d0e7ff;
        color: black;
        font-size: 18px;
        padding: 10px 20px;
        border: 2px solid #609BFF;
        border-radius: 18px;
        text-align: center;
        display: inline-block;
        cursor: pointer;
    }
    .custom-button:hover {
        background-color: #b0d4ff;
    }
    .stImage {
        padding: 0;
        margin: 0;
    }

    /* Floating button style */
    .floating-button {
        position: fixed;
        top: 50%; /* Adjust this value to position vertically */
        left: 20px; /* Distance from the left edge */
        transform: translateY(-50%); /* Center the button vertically */
        z-index: 1000; /* Make sure it appears on top of other elements */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add the floating button
st.markdown(
    """
    <div class="floating-button">
        <a href="https://www.example.com" target="_blank">
            <div class="custom-button">Přejít do nástroje</div>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.header("Průvodce pro ověřování produktových párů")

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
Je nám jasné, že nikdo nedosáhne 100% přesnosti, rádi bychom se tomu ale co nejvíce přiblížili. Abychom zajistili co nejvyšší kvalitu služby, některé produktové páry budou vyhodnocovány několikrát. 
To nám umožní průběžně vyhodnocovat přesnost kontroly. Dlouhodobě bychom chtěli dosahovat přesnosti nad 98 %.
""")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <a href="https://www.example.com" target="_blank">
        <div class="custom-button">Přejít do nástroje na kontrolu produktových párů</div>
    </a>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.header("Jak vyhodnotit nejednoznačné případy?")
st.write("""
Tato sekce obsahuje základní pravidla, která by měla být dodržována při ověřování shody produktů.
""")

# Updated function to include numbering
def create_rule_section(index, rule_name, description, image_path):
    st.markdown(f"### {index}. {rule_name}")  # Add the index to the rule name
    st.write(description)
    with st.expander(f"Příklad: {rule_name}"):
        st.image(image_path, caption=f"{rule_name} - Obrázek", use_column_width=True)

# Creating the rule sections with the updated image paths and numbering
create_rule_section(1, "Typ/vzhled", "Pokud produkt vypadá jinak (i když si jsou podobné), jde o jiný produkt.", "Images/Type2.jpg")
create_rule_section(2, "Barva", "Produkty musí mít vždy stejnou barvu i vzor.", "Images/Color2.jpg")
create_rule_section(3, "Velikost", "Produkty musí být stejně velké. Velikost je často dobrý ukazatel, pokud si podle obrázku nejste jistí, zda je produkt identický.", "Images/Size2.jpg")
create_rule_section(4, "Počet v balení", "Některé produktové páry mohou být logicky správně, ale v každém obchodě se produkt prodává v jiném množství (např. židle vs. 4 židle).", "Images/Count2.jpg")
create_rule_section(5, "Technické parametry", "Identicky vypadající produkty mohou mít jiné parametry: výkon, materiál, výdrž baterie, apod.", "Images/Parameter2.jpg")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    """
    <a href="https://www.example.com" target="_blank">
        <div class="custom-button">Přejít do nástroje na kontrolu produktových párů</div>
    </a>
    """,
    unsafe_allow_html=True
)
