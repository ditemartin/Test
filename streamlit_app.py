import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration to use a wide layout
st.set_page_config(layout="wide")

# Inject custom CSS to control the width of the main content
st.markdown(
    """
    <style>
    .main {
        max-width: 1000px; /* Set the desired width */
        margin: 0 auto;  /* Center align the content */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Generate sample data with more columns
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Description': ['A long description that makes the column too wide for the monitor.', 
                    'Another lengthy description that affects layout.', 
                    'Short description.', 
                    'Moderate length description.'],
    'Price': [100, 200, 300, 400],
    'Stock': [50, 60, 70, 80],
    'Category': ['Electronics', 'Clothing', 'Accessories', 'Home'],
    'Supplier': ['Supplier X', 'Supplier Y', 'Supplier Z', 'Supplier W'],
    'Location': ['Warehouse A', 'Warehouse B', 'Warehouse C', 'Warehouse D'],
    'Rating': [4.5, 4.0, 3.5, 4.2],
    'Discount': ['10%', '15%', '20%', '5%'],
    'Shipping Cost': [15, 20, 25, 30]
}

# Create a DataFrame with the expanded data
df = pd.DataFrame(data)

# Display the table with the wider layout
st.dataframe(df)
