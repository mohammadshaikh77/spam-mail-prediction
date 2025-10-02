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
spam_keywords = [
    # Money / prizes / get-rich
    "free", "freebie", "winner", "won", "congratulations", "claim your prize",
    "claim now", "gift card", "gift certificate", "cash bonus", "cash prize",
    "earn money", "make money", "get paid", "instant cash", "fast cash",
    "easy money", "double your", "passive income", "work from home",
    "no experience required", "earn from home", "extra income", "high income",
    "unlimited income",

    # Urgency / pressure
    "urgent", "act now", "act fast", "limited time", "expires",
    "offer expires", "last chance", "final notice",
    "immediate action required", "don’t miss out", "today only",

    # Click / links
    "click here", "click now", "click below", "follow this link",
    "visit our site", "open attachment", "download now",

    # Financial / loans / banking
    "pre-approved", "approved", "apply now", "low rate", "no credit check",
    "consolidate debt", "debt relief", "refinance", "loan approval",
    "mortgage", "payday loan", "instant approval", "unsecured loan",
    "wire transfer", "western union", "money transfer", "bank account",
    "account suspended", "verify your account", "update your account",
    "suspicious activity",

    # Phishing / security
    "verify account", "confirm your account", "account update required",
    "password reset", "reset your password", "unauthorized login",
    "verify identity", "security alert", "billing problem", "payment failed",

    # Attachments / malware
    "open attachment", "see attached", "attached invoice",
    "attached document", "attachment", "download attachment",

    # Scams / advance fee
    "you’ve been selected", "selected as a winner", "no obligation",
    "no strings attached", "tax-free", "inheritance", "urgent inheritance",
    "foreign lottery", "clearing house", "unexpected inheritance",
    "advance fee", "processing fee required", "send money",

    # Gambling / lottery
    "jackpot", "lottery", "lotto", "win big", "casino", "betting",
    "bet now", "spin to win", "free spins",

    # Crypto / investment
    "bitcoin", "crypto", "cryptocurrency", "investment opportunity",
    "guaranteed return", "high returns", "double your money",
    "ico", "token sale",

    # Health / pharma / adult
    "viagra", "cialis", "levitra", "phentermine", "prescription required",
    "no prescription", "buy medicine online", "weight loss", "lose weight",
    "miracle cure", "guaranteed cure", "herbal remedy", "penis enlargement",
    "sexual enhancement", "adult content", "porn", "xxx",

    # Sales / discounts
    "buy now", "order now", "limited supply", "low price", "lowest price",
    "cheap", "special promotion", "discount code", "coupon", "promo code",
    "wholesale", "clearance", "guaranteed", "risk-free",
    "money back guarantee", "satisfaction guaranteed",

    # Business / marketing spam
    "increase sales", "leads for sale", "outreach campaign",
    "marketing solution", "business opportunity", "work with us",
    "partner with", "consulting offer",

    # Sensitive data
    "social security", "ssn", "passport number", "driver license",
    "account number", "card number", "cvv", "credit card", "verify identity",

    # Common spam phrases
    "congratulations you have been selected", "urgent response required",
    "you have won", "you are a winner", "this is not a joke",
    "act immediately to claim", "click to remove", "you must respond within",
    "final reminder", "open immediately"
]

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

user_input = st.text_area("✍️ Enter the email/message here:")

if st.button("🔍 Check Mail"):
    if user_input.strip() != "":
        result = predict_mail(user_input)
        if result == "Spam Mail":
            st.error("🚨 This looks like a Spam Mail!")
        else:
            st.success("✅ This looks like a Ham Mail.")
    else:
        st.warning("⚠️ Please enter a message to check.")
