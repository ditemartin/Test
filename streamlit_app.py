import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Sample data
data = {
    "name": ["Website #27", "Website #29", "Website #19", "Website #4", "Website #15", "Website #1", "Website #12", "Website #23"],
    "products": [2, 5, 7, 13, 9, 12, 8, 13],
    "cheaper": [100, 40, 42.86, 23.08, 22.22, 16.67, 37.50, 38.46],
    "withinSensitivity": [0, 20, 14.29, 23.08, 44.44, 41.67, 12.50, 15.38],
    "moreExpensive": [0, 40, 42.85, 53.84, 33.34, 41.66, 50.00, 46.16],
    "priceIndex": [75.34, 89.93, 96.58, 96.64, 99.74, 100.39, 100.46, 100.58]
}

df = pd.DataFrame(data)

st.set_page_config(layout="wide")

st.title("Website #13: Cheaper Within price sensitivity More expensive")

# Original Table
st.header("Original Table")
st.dataframe(df.style.format({
    "cheaper": "{:.2f}%",
    "withinSensitivity": "{:.2f}%",
    "moreExpensive": "{:.2f}%",
    "priceIndex": "{:.2f}"
}))

# Side-by-side layout
col1, col2 = st.columns(2)

with col1:
    st.header("Basic Information")
    st.dataframe(df[["name", "products", "priceIndex"]].style.format({
        "priceIndex": "{:.2f}"
    }))

with col2:
    st.header("Percentage Breakdown")
    
    fig = go.Figure()
    
    for index, row in df.iterrows():
        fig.add_trace(go.Bar(
            y=[row["name"]],
            x=[row["cheaper"]],
            name="Cheaper",
            orientation="h",
            marker=dict(color="green"),
            showlegend=index == 0
        ))
        fig.add_trace(go.Bar(
            y=[row["name"]],
            x=[row["withinSensitivity"]],
            name="Within Sensitivity",
            orientation="h",
            marker=dict(color="yellow"),
            showlegend=index == 0
        ))
        fig.add_trace(go.Bar(
            y=[row["name"]],
            x=[row["moreExpensive"]],
            name="More Expensive",
            orientation="h",
            marker=dict(color="red"),
            showlegend=index == 0
        ))

    fig.update_layout(
        barmode="stack",
        height=400,
        margin=dict(l=0, r=0, t=0, b=0),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis_title="Percentage",
        yaxis_title="Website",
    )

    st.plotly_chart(fig, use_container_width=True)

    for index, row in df.iterrows():
        st.write(f"{row['name']}:")
        st.write(f"Cheaper: {row['cheaper']:.2f}% | Within Sensitivity: {row['withinSensitivity']:.2f}% | More Expensive: {row['moreExpensive']:.2f}%")

# Add some spacing
st.write("\n\n")

# Display raw data (optional)
if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(df)
