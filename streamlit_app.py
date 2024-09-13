import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Generating 500 normally distributed values between 0 and 200
np.random.seed(42)
values = np.random.normal(loc=100, scale=20, size=500)  # mean=100, std=20

# Clip the data to ensure the lowest value is 55 and highest is 145
values = np.clip(values, 55, 145)

# Defining 9 bins between 55 and 145
bins = np.linspace(55, 145, 10)

# Creating histogram data
hist_data = np.histogram(values, bins=bins)

# Adding hover information with number of items and range in parentheses on the second line, rounding values
hover_text = []
for i in range(len(hist_data[1]) - 1):
    if i == 0:
        hover_text.append(f'Počet: {hist_data[0][i]}<br>(<65)')  # First bin hover text
    elif i == len(hist_data[1]) - 2:
        hover_text.append(f'Počet: {hist_data[0][i]}<br>(>135)')  # Last bin hover text
    else:
        hover_text.append(f'Počet: {hist_data[0][i]}<br>({round(hist_data[1][i])} - {round(hist_data[1][i+1])})')

# Custom colors for the bins, ensuring the second yellow column turns red
color_map = ['#B9DC6B' if hist_data[1][i] < 95 else '#F96C6C' if hist_data[1][i] >= 105 else '#FFE897' 
             for i in range(len(hist_data[1]) - 1)]

# Add bars for all bins with hovertext showing count and rounded range
fig = go.Figure(go.Bar(
    x=[f"<65" if i == 0 else f">145" if i == len(bins)-2 else f"{int(round(hist_data[1][i]))} - {int(round(hist_data[1][i+1]))}" 
       for i in range(len(hist_data[1]) - 1)],
    y=hist_data[0],
    marker_color=color_map,  # Custom colors applied here
    hovertext=hover_text,
    hoverinfo="text",
))

# Update layout with custom title and axis labels, and remove the legend
fig.update_layout(
    title='Cenové porovnání s obchodem XXX',
    xaxis_title='Cenový index (nižší hodnoty znamenají, že jste levnější)',
    yaxis_title='Počet produktů',
    bargap=0.1,
    showlegend=False,  # Remove the legend
)

# Display the plot in Streamlit
st.plotly_chart(fig)
