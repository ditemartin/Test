import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Generating 500 normally distributed values between 0 and 200
np.random.seed(42)
values = np.random.normal(loc=100, scale=20, size=500)  # mean=100, std=20

# Creating custom bin edges
bins = [0, 65] + list(range(65, 145, 10)) + [145, 200]

# Creating a histogram
fig = go.Figure()

# Add bars for the histogram with green color for values below 95
fig.add_trace(go.Histogram(
    x=values[values < 95],
    xbins=dict(start=0, end=200, size=10),
    marker_color='green',
    name='Values below 95',
    autobinx=False
))

# Add bars for the histogram with red color for values above 105
fig.add_trace(go.Histogram(
    x=values[values > 105],
    xbins=dict(start=0, end=200, size=10),
    marker_color='red',
    name='Values above 105',
    autobinx=False
))

# Add bars for values between 95 and 105, keeping the color neutral
fig.add_trace(go.Histogram(
    x=values[(values >= 95) & (values <= 105)],
    xbins=dict(start=0, end=200, size=10),
    marker_color='orange',
    name='Values between 95 and 105',
    autobinx=False
))

# Update layout with custom bins
fig.update_layout(
    title='Histogram of Normally Distributed Values',
    xaxis_title='Values',
    yaxis_title='Frequency',
    bargap=0.1, 
    xaxis=dict(
        tickmode='array',
        tickvals=bins
    )
)

# Display the plot
st.plotly_chart(fig)
