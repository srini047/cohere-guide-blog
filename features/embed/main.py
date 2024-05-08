import streamlit as st
import cohere


@st.cache_data
def embed_content(key, input):
    co = cohere.Client(key)

    response = co.embed(
        texts=input.split(" "), model="embed-english-v3.0", input_type="classification"
    )

    return response
