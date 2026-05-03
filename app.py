import streamlit as st
import requests

st.title("Restaurant Voice Order Assistant")

user_input = st.text_input("Enter your order:")

if st.button("Submit"):
    response = requests.post(
        "http://127.0.0.1:8000/order",
        json={"text": user_input}
    )
    
    st.write("Response:")
    st.json(response.json())