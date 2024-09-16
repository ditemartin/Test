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
    .custom-button {
        background-color: #d0e7ff;  /* Slightly blue background */
        color: black;  /* Black text */
        font-size: 18px;  /* Slightly larger font size */
        padding: 10px 20px;
        border: 2px solid #007BFF;  /* Border to resemble the original button shape */
        border-radius: 8px;
        text-align: center;
        display: inline-block;
        cursor: pointer;
    }
    .custom-button:hover {
        background-color: #b0d4ff;  /* Slightly darker blue on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Header
st.header("Průvodce nástrojem pro ověřování shod")

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
 
Odměna je 150 Kč za 1.000 zkontrolovaných produktů.
""")

st.subheader("Přesnost")
st.write("""
Je nám jasné, že nikdo nedosáhne 100% přesnosti. Chceme ale vytvořit podmínky, které vám pomohou se k tomuto číslu co nejvíce přiblížit. Abychom zajistili co nejvyšší kvalitu služby, některé produktové páry budou vyhodnocovány několikrát. 
To nám umožní průběžně vyhodnocovat přesnost jednotlivých kontrolorů. Dlouhodobě by kontroloři měli dosahovat cca 98% přesnosti při vyhodnocování.
""")

# Add a slightly blue button using custom styling
button_clicked = st.markdown(
    """
    <a href="https://www.example.com" target="_blank">
        <div class="custom-button">Přejít do nástroje na kontrolu
