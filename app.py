import streamlit as st
from features.generate.main import generate_content

# Using "with" notation
with st.sidebar:
    st.title("Cohere AI")
    cohere_api_key = st.text_input(
        label="Cohere API Key",
        placeholder="Enter your API Key",
        type="password",
        help="https://dashboard.cohere.com/api-keys",
    )
    webpage = st.radio(
        "Available Features",
        ("Generate", "Chat", "Classify", "Summarize", "Detect Language"),
    )

if webpage == "Generate":
    st.title("Genereate")
    st.text(
        "Paste your question to generate generic content on all topics",
        help="https://docs.cohere.com/docs/command-beta",
    )
    model = st.selectbox(
        "Which model would you like to use?",
        ("command-light", "command", "command-nightly", "command-light-nightly"),
        help="https://docs.cohere.com/docs/command-beta#:~:text=Command%20is%20Cohere%27s,nightly%20to%20improve.",
    )
    max_tokens = st.number_input(
        label="Total tokens to use (limits the response)",
        min_value=50,
        max_value=400,
        value=200,
    )
    temperature = st.slider(
        "Model temperature to operate at (Optimal-0.7)", 0.1, 1.0, 0.1
    )

    input = st.text_input("Enter your prompt", max_chars=50)

    if st.button("Submit", type="primary") and cohere_api_key:
        answer = generate_content(cohere_api_key, input, model, max_tokens, temperature)
        st.success("Successful generation", icon="✅")
        st.write(answer)
    elif not cohere_api_key:
        st.error("Please provide API key", icon="❌")

elif webpage == "Classify":
    st.title("Classify")
    tab1, tab2 = st.tabs(["Example", "Custom"])

    with tab1:
        st.header("Hello..")

    with tab2:
        st.header("Example...")
