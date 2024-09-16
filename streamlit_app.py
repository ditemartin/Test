import streamlit as st
import pandas as pd

# Inject custom CSS to control the width of the main content
st.markdown(
    """
    <style>
    .main {
        max-width: 1400px; /* Adjust this value to set your desired width */
        margin: 0 auto;  /* Center align the content */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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

# Display the table without limiting the column width
st.dataframe(df)
