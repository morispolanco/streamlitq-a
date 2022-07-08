
import streamlit as st
import requests
import json
import pandas as pd
import numpy as np
import time
import os
import re

OPENAPI_KEY = os.environ['OPENAI_API_KEY']

# st.title('GPT-3 Q&A')

# st.write('This is a demo of the GPT-3 API. It is a simple Q&A app that uses the GPT-3 API to answer questions.')

# st.write('The GPT-3 API is a language model that uses machine learning to produce human-like text. It is the third version of OpenAI\'s Generative Pre-trained Transformer (GPT) language model. GPT-3 is trained on a dataset of hundreds of billions of words from the internet.')

# st.write('The GPT-3 API is currently in private beta. You can apply for access to the API [here](https://beta.openai.com/).')

# st.write('This app is built using Streamlit. You can find the source code [here](https://github.com/streamlit/demo-uber-nyc-pickups/blob/master/app.py).')

# st.write('You can find more information about GPT-3 [here](https://openai.com/blog/openai-api/).')

# st.write('You can find more information about Streamlit [here](https://www.streamlit.io/).')

# st.write('You can find more information about the GPT-3 API [here](https://beta.openai.com/).')
