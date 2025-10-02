# app.py
import streamlit as st
import joblib
import numpy as np

# Load the saved model and vectorizer
model = joblib.load('spam-ham.pkl')
vectorizer = joblib.load('tfidf.pkl')

# App title
st.title("📧 Spam Mail Prediction")

# User input
input_mail = st.text_area("Enter the message here:")

if st.button("Predict"):
    # Transform input like in your code
    input_data_features = feature_extraction.transform([input_mail])
    prediction = model.predict(input_data_features)
    
    # Display result exactly like your snippet
    if prediction[0] == 1:
        st.success("✅ Ham Mail")
    else:
        st.error("⚠️ Spam Mail")