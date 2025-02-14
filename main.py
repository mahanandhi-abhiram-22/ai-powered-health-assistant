import streamlit as st
from transformers import pipeline
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# ... (rest of your code) ...

from pyngrok import ngrok
import os

# Get your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken
# and set it as an environment variable
os.environ["NGROK_AUTH_TOKEN"] = "2s3tXOMvzlq0aXwvwJ4mKqrPkuM_25vYyU5GiShAKrmEDgdnY"  # Replace with your actual authtoken

# Run Streamlit app
os.system("streamlit run app.py &")

# Expose the app through ngrok
public_url = ngrok.connect(8501)  # Streamlit's default port
print(f"Streamlit app running at: {public_url}")