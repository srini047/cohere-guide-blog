import streamlit as st
import cohere


@st.cache_data
def detect_language(key, input):
    co = cohere.Client(key)
    texts = [
        "Hello from Cohere!",
        "مرحبًا من كوهير!",
        "Hallo von Cohere!",
        "Bonjour de Cohere!",
        "¡Hola desde Cohere!",
        "Olá do Cohere!",
        "Ciao da Cohere!",
        "您好，来自 Cohere！",
        "कोहेरे से नमस्ते!",
    ]
    response = co.embed(
        texts=texts,
        input_type="classification",
        embedding_types=["float"],
        model="embed-multilingual-v3.0",
    )
    embeddings = response.embeddings.float
    print(embeddings[0][:5])
