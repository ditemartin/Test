import streamlit as st
import pandas as pd

# Inject custom CSS to control the width of the main content
st.markdown(
    """
    <style>
    .main {
        max-width: 1200px; /* Adjust this value to set your desired width */
        margin: 0 auto;  /* Center align the content */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Your application code goes here
st.title("Custom Width Streamlit App")

# Sample DataFrame
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Description': ['A long description that makes the column too widemn too widemn too widemn too wide for the monitor.', 
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
    max-width: 600px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
</style>
"""

# Display the table with custom CSS
st.markdown(css, unsafe_allow_html=True)
st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)
