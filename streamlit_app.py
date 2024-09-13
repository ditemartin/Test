import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Generating 500 normally distributed values between 0 and 200
np.random.seed(42)
values = np.random.normal(loc=100, scale=20, size=500)  # mean=100, std=20

# Defining custom bin edges
bins = [0, 65] + list(range(65, 145, 10)) + [145, 200]

# Creating histogram data
hist_data = np.histogram(values, bins=bins)

# Creating a plotly figure
fig = go.Figure()

# Define bin centers for bar plot
bin_centers = 0.5 * (hist_data[1][1:] + hist_data[1][:-1])

# Add bars for values below 95 (green)
fig.add_trace(go.Bar(
    x=bin_centers[bin_centers < 95],
    y=hist_data[0][bin_centers < 95],
    marker_color='green',
    name='Values below 95'
))

# Add bars for values between 95 and 105 (orange)
fig.add_trace(go.Bar(
    x=bin_centers[(bin_centers >= 95) & (bin_centers <= 105)],
    y=hist_data[0][(bin_centers >= 95) & (bin_centers <= 105)],
    marker_color='orange',
    name='Values between 95 and 105'
))

# Add bars for values above 105 (red)
fig.add_trace(go.Bar(
    x=bin_centers[bin_centers > 105],
    y=hist_data[0][bin_centers > 105],
    marker_color='red',
    name='Values above 105'
))

# Update layout with custom bins and axis titles
fig.update_layout(
    title='Histogram of Normally Distributed Values with Custom Bins',
    xaxis_title='Values',
    yaxis_title='Frequency',
    bargap=0.1,
    xaxis=dict(tickmode='array', tickvals=bins),
)

# Display the plot in Streamlit
st.plotly_chart(fig)
