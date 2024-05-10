import streamlit as st
from features.generate.main import generate_content
from features.classify.main import classify_content
from features.summarize.main import summarize_content
from features.embed.main import embed_content

# from features.detect.main import detect_language

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
        ("Classify", "Embeddings", "Generate", "Summarize"),
    )

if webpage == "Generate":
    st.title("Genereate")
    st.text(
        "Paste your question to generate generic content on all topics",
        help="https://docs.cohere.com/docs/migrating-from-cogenerate-to-cochat",
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
    st.text("Sentiment Analysis Classification {Positve, Negative, Neurtral}")

    model = st.selectbox(
        "Which model would you like to use?",
        ("embed-english-v2.0", "embed-multilingual-v2.0", "embed-english-light-v2.0"),
        help="https://docs.cohere.com/reference/classify",
    )

    text = st.text_input("Enter the text to classify", max_chars=50)
    input = []
    input.append(text)

    if st.button("Submit", type="primary") and cohere_api_key:
        answer = classify_content(cohere_api_key, input)
        st.success("Successful generation", icon="✅")
        st.text(answer)
    elif not cohere_api_key:
        st.error("Please provide API key", icon="❌")

elif webpage == "Summarize":
    st.title("Summarize")

    model = st.selectbox(
        "Which model would you like to use?",
        ("command-light", "command", "command-nightly", "command-light-nightly"),
        help="https://docs.cohere.com/reference/summarize-2",
    )

    format = st.selectbox(
        "How do you want the model to draft the summary?",
        ("auto", "bullets", "paragraph"),
        help="https://docs.cohere.com/reference/summarize-2",
    )

    extractiveness = st.selectbox(
        "How do you want the model to paraphrase?",
        ("auto", "low", "medium", "high"),
        help="https://docs.cohere.com/reference/summarize-2",
    )

    temperature = st.slider(
        "Model temperature to operate at (Optimal range 0-1)", 0.0, 5.0, 0.1
    )

    input = st.text_area("Paste the passage in (English)", max_chars=1500)

    if st.button("Submit", type="primary") and cohere_api_key:
        answer = summarize_content(
            cohere_api_key, input, model, extractiveness, format, temperature
        )
        st.success("Successful generation", icon="✅")
        st.markdown(answer)
    elif len(input) < 250:
        st.error("Length of the passage must be atleast 250 words", icon="❌")
    elif not cohere_api_key:
        st.error("Please provide API key", icon="❌")

elif webpage == "Embeddings":
    st.title("Embed Text", help="https://docs.cohere.com/reference/embed")

    input = st.text_area(
        "Paste the passage in (English)",
        max_chars=50,
    )

    if st.button("Submit", type="primary") and cohere_api_key:
        answer = embed_content(cohere_api_key, input)
        st.success("Successful generation", icon="✅")
        st.markdown(answer)
    elif not cohere_api_key:
        st.error("Please provide API key", icon="❌")

# Deprecated
# elif webpage == "Detect Language":
#     st.title("Detect Language")
#     st.markdown(
#         "This works on the fact that input if input is detected as English, it is routed to the English Model, else it is routed to Multilingual Embed Model."
#     )

#     text = st.text_input("Enter the text to detext language", max_chars=50)
#     input = []
#     input.append(text)

#     if st.button("Submit", type="primary") and cohere_api_key and text:
#         answer = detect_language(cohere_api_key, input)
#         st.success("Successful generation", icon="✅")
#         st.markdown("Detected language: " + answer)
#     elif not cohere_api_key:
#         st.error("Please provide API key", icon="❌")
