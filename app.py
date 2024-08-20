#!/usr/bin/env python
# coding: utf-8

# In[36]:


import streamlit as st
import pandas as pd
import numpy as np

# Title for the app
st.title('Simple Streamlit App')

# Creating a dataframe
df = pd.DataFrame({
    'First Column': [1, 2, 3, 4],
    'Second Column': [10, 20, 30, 40]
})

# Displaying the dataframe
st.write("Here is our dataframe:")
st.dataframe(df)

# Adding an interactive widget
x = st.slider('Select a value for x', 0, 100, 50)
st.write(f'The value of x is {x}')

# Simple plot
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)







