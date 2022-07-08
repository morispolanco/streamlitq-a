import streamlit as st
import requests
import json

st.title("GPT-3 Q&A")

prompt = st.text_input("Prompt")

url = "https://api.openai.com/v1/engines/davinci/completions"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + ["OPENAI.API_KEY"]
}

data = {
    "prompt": prompt,
    "max_tokens": 50,
    "temperature": 0.7,
    "top_p": 0.9,
    "n": 1,
    "stream": False,
    "logprobs": None,
    "stop": "\n"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

response_json = response.json()

st.write(response_json["choices"][0]["text"])

