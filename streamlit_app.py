import streamlit as st

st.set_page_config(page_title="Průvodce pro ověřování produktových párů", layout="wide")

# Adjust the page width and create a sticky header with a button
st.markdown(
    """
    <style>
    .main {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Sticky container for header and button */
    .sticky-container {
        position: fixed;
        top: 60px; /* Adjust this value to move the sticky container lower */
        left: 50%;
        transform: translateX(-50%);
        width: 1200px; /* Match the width of the main content */
        background-color: white; /* Match background to page */
        z-index: 1000; /* Make sure it appears on top */
        padding: 10px 20px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Add a subtle shadow for separation */
        display: flex;
        justify-content: space-between;
        align-items: center;
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
    
    /* Add margin to the top of the main content to avoid being hidden behind the sticky header */
    .content {
        margin-top: 120px; /* Increased to provide more space for the sticky header */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add the sticky header with the button
st.markdown(
    """
    <div class="sticky-container">
        <h1>Průvodce pro ověřování produktových párů</h1>
        <a href="https://console.deepscout.ai/" target="_blank">
            <div class="custom-button">Přejít do nástroje</div>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Add some margin to the top of the main content
st.markdown('<div class="content">', unsafe_allow_html=True)

st.subheader("Jak na to?")
st.write("""
V některých případech to je velmi jednoduché a shoda/rozdíl jsou jasné na první pohled. Občas je třeba produkty prozkoumat detailně.
- Pokud si nejste jistí, přepněte na zobrazení **Porovnávat weby**, kde najdete další detaily. Na web jednotlivých eshopů se také můžete dostat proklikem přes název produktu.
- Pokud si ani po bližším prozkoumání nejste jistí, zda jsou produkty totožné, použijte tlačítko **Nejsem si jistý**.
- Jestliže uděláte chybu, můžete se vrátit tlačítkem **Zpět**.
- Proces kontroly a důležité faktory se liší podle typu kontrolovaného zboží. U elektroniky sledujte jiné parametry než u koberců.
- Při kontrole často mohou pomoci produktové kódy od dodavatelů.

""")

st.subheader("Filtry")
st.write("""
Produktové páry můžete několika různými způsoby řadit a filtrovat:
- **Náhodné páry** 
- **Rizikové páry** nejpravděpodobnější chyby
- **Pravděpodobné nepáry** produkty, které jen těsně nebyly vyhodnocené jako pár, ale mají vysokou pravděpodobnost, že by mohly být
- **Nejisté páry** jsou páry, které jste dřív označili jako **Nejsem si jistý**
- **Cenové anomálie** jsou páry, u kterých vidíme největší cenové rozdíly
""")

# Add two line breaks before "Jak vyhodnotit"
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Přesnost")
st.write("""
Je nám jasné, že nikdo nedosáhne 100% přesnosti, rádi bychom se tomu ale co nejvíce přiblížili. Abychom zajistili co nejvyšší kvalitu služby, některé produktové páry budou vyhodnocovány několikrát. 
To nám umožní průběžně vyhodnocovat přesnost kontroly. Dlouhodobě bychom chtěli dosahovat přesnosti nad 98 %.
""")

# Add two line breaks before "Jak vyhodnotit"
st.markdown("<br>", unsafe_allow_html=True)

st.header("Jak vyhodnotit nejednoznačné případy?")
st.write("""
Tato sekce obsahuje základní pravidla, která by měla být dodržována při ověřování shody produktů.
""")

# Function to create numbered rule sections
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
create_rule_section(6, "Nesymetrické informace", "Pokud je jeden produkt jasně specifikovaný (např velikost L, nebo materiál) a druhý nabízí na stejné URL adrese výběr z více variant, které jsou stejně naceněné, jde o stejný produkt. Pokud je každý varianta na jiné URL adrese, nebo má jinou cenu, nejde o stejný produkt.", "Images/Size_symmetry.png")

# Close the content div
st.markdown('</div>', unsafe_allow_html=True)
