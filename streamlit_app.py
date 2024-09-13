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

# Adding hover information for bin ranges
hover_text = [f'Range: {hist_data[1][i]} - {hist_data[1][i+1]}' for i in range(len(hist_data[1]) - 1)]

# Add bars for values below 95 (green)
fig.add_trace(go.Bar(
    x=bin_centers[bin_centers < 95],
    y=hist_data[0][bin_centers < 95],
    marker_color='green',
    name='Values below 95',
    hovertext=[hover_text[i] for i in range(len(hover_text)) if bin_centers[i] < 95],
    hoverinfo="text"
))

# Add bars for values
