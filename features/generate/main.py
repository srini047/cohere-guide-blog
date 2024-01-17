import streamlit as st
import cohere


@st.cache_data
def generate_content(key, input, model, max_tokens, temp):
    co = cohere.Client(key)
    response = co.generate(
        model=model, prompt=input, temperature=temp, max_tokens=max_tokens
    )
    return response.generations[0].text
