import streamlit as st
import pickle
from predictor import predict_sentiment # A function imported from predictor.py to handle prediction logic.

# Load model and vectorizer
with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('models/vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Streamlit UI
st.set_page_config(page_title="Twitter Sentiment Classifier", layout="centered")

st.title("Twitter Sentiment Classifier")
st.write("Enter a tweet below to classify it as Positive or Negative.")

tweet_input = st.text_area("Tweet:", "", height=150)        # "" states that there are no default text

if st.button("Classify"):
    if tweet_input.strip() == "":                           #checks if empty, then raises warning 
        st.warning("Please enter a tweet to classify.")
    else:
        result = predict_sentiment(tweet_input, model, vectorizer)
        st.success(f"Sentiment: {result.upper()}")
