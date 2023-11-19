import streamlit as st
import random
import altair as alt
import numpy as np
import pandas as pd

st.header('Homework 1')

st.markdown(
"**QUESTION 1**: In previous homeworks you created dataframes from random numbers.\n"
"Create a datframe where the x axis limit is 100 and the y values are random values.\n"
"Print the dataframe you create and use the following code block to help get you started"
)

x_limit = 100
x_axis = np.arange(0, x_limit, 1)
y_data = [random.random() for value in x_axis]

df = pd.DataFrame({'x_axis': x_axis,
                     'y_data': y_data})
st.write(df)


st.code(
''' 
x_limit = 

# List of values from 0 to 100 each value being 1 greater than the last
x_axis = np.arange()

# Create a random array of data that we will use for our y values
y_data = []

df = pd.DataFrame({'x': x_axis,
                     'y': y_data})
st.write(df)''',language='python')


st.markdown(
"**QUESTION 2**: Using the dataframe you just created, create a basic scatterplot and Print it.\n"
"Use the following code block to help get you started."
)


st.title('Testing the waters with Streamlit and Altair Charts')
# depict scatter plot
scatter = (
    alt.Chart(df)
    .encode( x='x_axis',y='y_data',size = 'x_axis', color='x_axis')
    .mark_circle()
)

st.altair_chart(scatter, theme="streamlit", use_container_width=True)


st.code(
''' 
scatter = alt.Chart().mark_point().encode()

st.altair_chart(scatter, use_container_width=True)''',language='python')


st.markdown(
"**QUESTION 3**: Lets make some edits to the chart by reading the documentation on Altair.\n"
"https://docs.streamlit.io/library/api-reference/charts/st.altair_chart.  "
"Make 5 changes to the graph, document the 5 changes you made using st.markdown(), and print the new scatterplot.  \n"
"To make the bullet points and learn more about st.markdown() refer to the following discussion.\n"
"https://discuss.streamlit.io/t/how-to-indent-bullet-point-list-items/28594/3"
)

st.markdown("The five changes I made were.....")
st.markdown("""
The 5 changes I made were:
- Change 1 changed column/label name to x_axis
- Change 2 changed column/label name to y_data
- Change 3 added size
- Change 4 added color
- Change 5 added title
""")



st.markdown(
"**QUESTION 4**: Explore on your own!  Go visit https://altair-viz.github.io/gallery/index.html.\n "
"Pick a random visual, make two visual changes to it, document those changes, and plot the visual.  \n"
"You may need to pip install in our terminal for example pip install vega_datasets "
)
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

st.markdown("""
The 2 changes I made were:
- Change 1:  create a heatmap/with new random numbers
- Change 2:  change color theme to be temperature
"""
)

