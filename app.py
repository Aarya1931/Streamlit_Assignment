import streamlit as st
from textblob import TextBlob

# Title of the web app
st.title("Basic Sentiment Analysis")

# User input
user_input = st.text_area("Enter text for sentiment analysis:")

# Analyze sentiment
if st.button("Analyze"):
    if user_input:
        analysis = TextBlob(user_input)
        sentiment = analysis.sentiment.polarity

        # Determine sentiment category
        if sentiment > 0:
            st.success("The sentiment is Positive 😊")
        elif sentiment < 0:
            st.error("The sentiment is Negative 😞")
        else:
            st.info("The sentiment is Neutral 😐")
    else:
        st.warning("Please enter some text!")
