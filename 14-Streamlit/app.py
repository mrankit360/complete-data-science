#### Introduction to Streamlit
'''Streamlit is an open-source app framework for Machine Learning and Data Science projects. 
It allows you to create beautiful web applications for your machine learning and 
data science projects with simple Python scripts.'''

import streamlit as st
import pandas as pd
import numpy as np

#Title of The application
st.title("Hello Streamilt")

#Header
st.header("This is header")

## Diplay a Simple Text
st.write("This is a simple text")

#Take input
name = st.text_input("Enter Your name: ")
st.write("Hello ", name)

if st.button("Click Me"):
    st.write("Button Clicked")

#slider
age = st.slider("Select Your age", 1,100)
st.write("Your age: ",age)

#Display Data

data = {
    "Name":["Ankit","Krish","Aman"],
    "Age":[20,30,27]
}
df = pd.DataFrame(data)
st.dataframe(df)

#Charts Example
charts_data = pd.DataFrame({
    'numbers':[1,2,3,4],
    'values':[10,20,30,40]
})

st.line_chart(charts_data)

options = ["c++","python","java","javascript"]
choice = st.selectbox("Your Favourite Subject is: ",options)
st.write(f"You Selected: {choice}")

option = ['Data Scientist', 'Mern Developer', 'Web3']
dream=st.selectbox("What You Want To Become", option)
st.write(f'You choose:', dream)