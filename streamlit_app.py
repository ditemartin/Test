import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Sample DataFrame
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Description': ['A long description that makes the column too wide for the monitor.', 
                    'Another lengthy description that affects layout.', 
                    'Short description.', 
                    'Moderate length description.'],
    'Price': [100, 200, 300, 400]
}
df = pd.DataFrame(data)

# Create CSS to limit the width of the 'Description' column
css = """
<style>
table {
    width: 100%;
}

table th:nth-child(2), table td:nth-child(2) {
    max-width: 150px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
</style>
"""

# Display the table with custom CSS
st.markdown(css, unsafe_allow_html=True)
st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)
