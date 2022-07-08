import streamlit as st
import requests
import json

st.title("GPT-3 Chat App")

st.write("""

This is a simple chat app to showcase the API capabilities of GPT-3.

""")

user_prompt = st.text_input("Enter your message:")

if st.button("Submit"):
    response = requests.post(
        "https://api.openai.com/v1/engines/davinci/completions",
        data=json.dumps({
            "prompt": user_prompt,
            "max_tokens": 50,
            "temperature": 0.7,
            "top_p": 0.9,
        }),
        headers={
            "Content-Type": "application/json",
            "Authorization": "OPENAI.API_KEY",
        },
    )
    response = response.json()
    st.write(response["choices"][0]["text"])
