import textblob
from textblob import TextBlob
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
import streamlit as st


def convert_low(text):
    return text.lower()


def remove_stopwords(text):
    x = []
    for i in text.split():
        if i not in stopwords.words('english'):
            x.append(i);
    y = x[:]
    x.clear()
    return y;


def join_back(text):
    return ' '.join(text)


def stem_word(text):
    y = []
    for i in text:
        y.append(ps.stem(i))
    z = y[:]
    return z


def remove_special(text):
    x = ''
    for i in text:
        if i.isalnum():
            x = x + i
        else:
            x = x + ' '
    return x


def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0.0:


        return "Positive"
    elif sentiment < 0.0:

        return "Negative"
    else:

        return "Neutral"


def printsentiment(text):
    x = convert_low(text)
    y = remove_special(x)
    z = remove_stopwords(y)
    k = join_back(z)
    j=get_sentiment(k)
    return j



st.title('Sentimental analyzer')
x = st.text_input("Enter Your Review")
if st.button('Show Sentiment'):
    st.text(printsentiment(x))
