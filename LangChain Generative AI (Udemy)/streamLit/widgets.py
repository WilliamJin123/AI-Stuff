import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")

name = st.text_input("Enter your name: ")

age = st.slider("Select your age: ", 0, 100, 25)
st.write(f"your age is {age}")
if name:
    st.write(f"Hello, {name}")

options = ['a','b','c','d']
choice = st.selectbox("choose an option", options)
st.write(f'you selected {choice}')

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_f = st.file_uploader("Choose a CSV", type="csv")
if uploaded_f:
    df = pd.read_csv(uploaded_f)
    st.write(df)


