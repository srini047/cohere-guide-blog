import streamlit as st
import cohere


@st.cache_data
def rerank_documents(key, docs, model, query):
    co = cohere.Client(key)

    response = co.rerank(
        documents=docs.split(". "),
        model=model,
        query=query,
        return_documents=True
    )

    return response.results
