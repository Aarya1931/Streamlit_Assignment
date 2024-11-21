import streamlit as st
from textblob import TextBlob

st.title("Basic Sentiment Analysis App")
st.subheader("Enter your text below to analyze the sentiment:")

user_input = st.text_area("Enter Text:")
if st.button("Analyze"):
    if user_input:
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity
        if polarity > 0:
            st.success("The sentiment is Positive 😊")
        elif polarity < 0:
            st.error("The sentiment is Negative 😟")
        else:
            st.info("The sentiment is Neutral 😐")
    else:
        st.warning("Please enter some text for analysis!")
