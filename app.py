# app.py
import streamlit as st
import joblib
import numpy as np

# Load the saved model and vectorizer
model = joblib.load('spam-ham.pkl')
feature_extraction = joblib.load('tfidf.pkl')

# App title
st.title("📧 Spam Mail Prediction")

# User input
input_mail = ['URGENT! You have won a 1 week FREE membership in our Â£100,000 Prize Jackpot! Txt the word: CLAIM to No: 81010 T&C www.dbuk.net LCCLTD']
spam_keywords = ['free', 'win', 'prize', 'click', '£', 'x', 'msg', 'subscribe', 'urgent', 'cash']

def predict_mail(mail_text):
    # Check for spam keywords first
    if any(word.lower() in mail_text.lower() for word in spam_keywords):
        return 'Spam Mail'
    # Otherwise use ML model
    features = feature_extraction.transform([mail_text])
    pred = model.predict(features)
    # prediction = predict_mail(input_mail[0]) # This line calls the function recursively, which is likely not intended and can be removed
    # print(prediction) # This line will print the result inside the function, but we want to return the result
    return 'Ham Mail' if pred[0] == 1 else 'Spam Mail'
