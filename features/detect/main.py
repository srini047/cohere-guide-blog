import streamlit as st
import cohere


@st.cache_data
def detect_language(key, input):
    co = cohere.Client(key)
    response = co.detect_language(texts=input)

    return response.results[0].language_name
