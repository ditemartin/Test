import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Generate random prices for 5 stores over the last 90 days
dates = pd.date_range(end=pd.Timestamp.today(), periods=7, freq='D')
stores = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E']
product_urls = [f"https://example.com/product-{i}" for i in range(1, 6)]

# Function to generate random price data with small fluctuations
def generate_price_data(size, start_price=150, price_range=(100, 250)):
    prices = [start_price]
    for _ in range(size - 1):
        prices.append(max(min(prices[-1] + np.random.randint(-10, 10), price_range[1]), price_range[0]))
    return prices

# Create DataFrame for prices across all stores
df = pd.DataFrame({store: generate_price_data(len(dates)) for store in stores}, index=dates)
df = df.reset_index().melt(id_vars=['index'], var_name='Store', value_name='Price')
df.rename(columns={'index': 'Date'}, inplace=True)
df['Product URL'] = np.random.choice(product_urls, size=len(df))

# Default date range (last 3 months)
start_date = pd.Timestamp.today() - pd.Timedelta(days=90)
end_date = pd.Timestamp.today()

# UI for filtering by product URL and date range (on one row)
st.header("Filter Options")
selected_url = st.selectbox("", options=product_urls, label_visibility="collapsed")
col1, col2 = st.columns(2)
with col1:
    start_date_input = st.date_input("Start Date", value=start_date)
with col2:
    end_date_input = st.date_input("End Date", value=end_date)

# Filter the DataFrame based on selections
filtered_data = df[(df['Date'] >= pd.to_datetime(start_date_input)) & 
                   (df['Date'] <= pd.to_datetime(end_date_input)) & 
                   (df['Product URL'] == selected_url)]

# Plot price trends
fig = px.line(filtered_data, x='Date', y='Price', color='Store', line_shape='spline',
              title='Vývoj cen u produktu XXX', labels={'Price': 'Cena', 'Store': ''})
fig.update_xaxes(dtick="M7", tickformat="%d-%m-%Y")  # Weekly ticks in dd-mm-yyyy format
fig.update_yaxes(tickprefix="", tickformat=",.0f Kč")
st.plotly_chart(fig)

# Calculate price change percentages for each store (first to last value) and display below the chart
st.subheader("Celková cenová změna")
for store in stores:
    store_data = filtered_data[filtered_data['Store'] == store]
    if len(store_data) > 1:
        percent_change = ((store_data['Price'].iloc[-1] - store_data['Price'].iloc[0]) / store_data['Price'].iloc[0]) * 100
        color = 'green' if percent_change < 0 else 'red'
        st.markdown(f"**{store}:** <span style='color:{color}'>{percent_change:.2f}%</span>", unsafe_allow_html=True)
