import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy.interpolate import make_interp_spline

# Generating random dates for the X-axis (weekly)
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

# Apply cubic spline interpolation for smooth lines
interpolated_data = pd.DataFrame()
for store in stores:
    store_data = filtered_data[filtered_data['Store'] == store]
    if len(store_data) > 1:
        x_new = np.linspace(store_data['Date'].map(pd.Timestamp.toordinal).min(),
                            store_data['Date'].map(pd.Timestamp.toordinal).max(), 300)
        spline = make_interp_spline(store_data['Date'].map(pd.Timestamp.toordinal), store_data['Price'], k=3)
        y_new = spline(x_new)
        temp_df = pd.DataFrame({'Date': pd.to_datetime(x_new, origin='julian', unit='D'), 
                                'Price': y_new, 'Store': store})
        interpolated_data = pd.concat([interpolated_data, temp_df])

# Plot the smooth lines
fig = px.line(interpolated_data, x='Date', y='Price', color='Store',
              title='Vývoj cen u produktu XXX',
              labels={'Price': 'Cena (Kč)', 'Date': 'Date', 'Store': 'Store'})

# Update x-axis frequency to weekly and y-axis format to "Kč"
fig.update_xaxes(dtick="M1", tickformat="%d-%b")  # Show monthly, you can modify for weekly
fig.update_yaxes(tickprefix="", tickformat=",.0f Kč")

# Display the plot
st.plotly_chart(fig)

# Calculate percentage change in price for each store
st.subheader("Price Change Percentages")
price_change = []
for store in stores:
    store_data = filtered_data[filtered_data['Store'] == store].copy()
    store_data['Percent Change'] = store_data['Price'].pct_change() * 100  # Calculate percentage change
    store_data.dropna(inplace=True)  # Drop first row because there's no previous value to compare

    # Display the percentage changes
    for _, row in store_data.iterrows():
        color = 'green' if row['Percent Change'] < 0 else 'red'
        st.markdown(f"**{row['Store']} on {row['Date'].date()}:** "
                    f"<span style='color:{color}'>{row['Percent Change']:.2f}%</span>", unsafe_allow_html=True)

# Show the filtered data as a table (optional)
st.write("Filtered Data", filtered_data)
