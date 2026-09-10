import streamlit as st

st.title("My First Streamlit App")

st.write("Hello! This is my first Streamlit application.")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Welcome, {name}!")