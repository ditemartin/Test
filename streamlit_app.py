import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Generating 500 normally distributed values between 0 and 200
np.random.seed(42)
values = np.random.normal(loc=100, scale=20, size=500)  # mean=100, std=20

# Clip the data to ensure the lowest value is 55 and highest is 155
values = np.clip(values, 55, 155)

# Defining custom bin edges
bins = [55, 65] + list(range(65, 145, 10)) + [145, 155]

# Creating histogram data
hist_data = np.histogram(values, bins=bins)

# Creating a plotly figure
fig = go.Figure()

# Define bin centers for bar plot
bin_centers = 0.5 * (hist_data[1][1:] + hist_data[1][:-1])

# Adding hover information with number of items and range in parentheses on the second line
hover_text = []
for i in range(len(hist_data[1]) - 1):
    if i == 0:
        hover_text.append(f'Count: {hist_data[0][i]}<br>(<65)')  # First bin hover text
    elif i == len(hist_data[1]) - 2:
        hover_text.append(f'Count: {hist_data[0][i]}<br>(>145)')  # Last bin hover text
    else:
        hover_text.append(f'Count: {hist_data[0][i]}<br>({hist_data[1][i]} - {hist_data[1][i+1]})')

# Uniform width for all bins
uniform_width = 10  # Set the desired uniform width for all bins

# Custom colors for the bins
color_map = ['#B9DC6B' if center < 95 else '#F96C6C' if center > 105 else '#FFE897' for center in bin_centers]

# Add bars for all bins with uniform bin widths and hovertext showing count and range
fig.add_trace(go.Bar(
    x=bin_centers,
    y=hist_data[0],
    marker_color=color_map,  # Custom colors applied here
    hovertext=hover_text,
    hoverinfo="text",
    width=[uniform_width] * len(bin_centers)  # Apply uniform width to all bins
))

# Update layout with custom bins and axis titles, and remove the legend
fig.update_layout(
    title='Histogram of Normally Distributed Values (Clipped) with Custom Colors',
    xaxis_title='Values',
    yaxis_title='Frequency',
    bargap=0.1,
    showlegend=False,  # Remove the legend
    xaxis=dict(tickmode='array', tickvals=bins),
)

# Display the plot in Streamlit
st.plotly_chart(fig)
