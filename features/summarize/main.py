import streamlit as st
import cohere


@st.cache_data
def summarize_content(key, input, model, extractiveness, format, temp):
    co = cohere.Client(key)
    response = co.summarize(
        text=input,
        model=model,
        extractiveness=extractiveness,
        format=format,
        temperature=temp,
    )

    return response.summary
