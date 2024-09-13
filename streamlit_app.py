import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Simulate dynamic price fluctuations using a random walk for 5 stores over a week
dates = pd.date_range(start='2023-09-01', periods=7, freq='D')
stores = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']

# Function to generate random walk for price data between 100 and 250
def generate_price_data(days, start_price=150, price_range=(100, 250)):
    price_data = [start_price]
    for _ in range(days - 1):
        change = np.random.randint(-10, 10)  # daily price change
        new_price = price_data[-1] + change
        new_price = max(min(new_price, price_range[1]), price_range[0])  # constrain within price range
        price_data.append(new_price)
    return price_data

# Generate dynamic prices for each store
price_data = {store: generate_price_data(len(dates)) for store in stores}
df = pd.DataFrame(price_data, index=dates).reset_index()
df = df.melt(id_vars=['index'], var_name='Store', value_name='Price')

# Rename the columns
df.rename(columns={'index': 'Date'}, inplace=True)

# Simulate product URLs for filtering
product_urls = [f"https://example.com/product-{i}" for i in range(1, 6)]
df['Product URL'] = np.random.choice(product_urls, size=len(df))

# Sidebar filters
st.sidebar.header("Filter Options")
selected_url = st.sidebar.selectbox("Select Product URL", options=product_urls)
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime('2023-09-01'))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime('2023-09-07'))

# Filter data by date and product URL
filtered_data = df[(df['Date'] >= pd.to_datetime(start_date)) & 
                   (df['Date'] <= pd.to_datetime(end_date)) & 
                   (df['Product URL'] == selected_url)]

# Plot the price trends
fig = px.line(filtered_data, x='Date', y='Price', color='Store',
              title=f'Price Trends for {selected_url}',
              labels={'Price': 'Price (in currency)', 'Date': 'Date', 'Store': 'Store'})

# Display the plot
st.plotly_chart(fig)

# Show the filtered data as a table (optional)
st.write("Filtered Data", filtered_data)
