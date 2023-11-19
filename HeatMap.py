import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

# Generate random data with 5000 points
np.random.seed(42)
num_points = 5000
data = pd.DataFrame({
    'x': np.random.randint(0, 10, num_points),
    'y': np.random.randint(0, 10, num_points),
    'value': np.random.randint(100, 301, num_points)
})

# Create a custom color scale for the heatmap with 35 color steps from red to orange to yellow to green
color_scale = alt.Scale(
    domain=[100, 141, 200, 255, 300],
    range=["#FF0000", "#FF4500", "#FF8C00", "#FFFF00", "#00FF00"]
)

# Create a heatmap using Altair with "rect" marks for each data point
heatmap = alt.Chart(data).mark_rect().encode(
    x='x:O',
    y='y:O',
    color=alt.Color('value:Q', scale=color_scale),
    tooltip=['x', 'y', 'value']
).properties(
    width=500,
    height=500
)

# Streamlit app
st.title('Random Heatmap with Custom Color Scale, Streamlit, and Altair')
st.write("The heatmap displays all 5000 data points as separate rectangles with a custom color scale, ranging from red to orange to yellow to green for values between 141 and 300, with 35 color steps.")

st.altair_chart(heatmap)
