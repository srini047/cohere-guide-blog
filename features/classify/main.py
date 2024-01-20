import streamlit as st
import cohere
from cohere.responses.classify import Example


@st.cache_data
def classify_content(key, input, model):
    co = cohere.Client(key)
    examples = [
        Example("I'm so proud of you", "positive"),
        Example("What a great time to be alive", "positive"),
        Example("That's awesome work", "positive"),
        Example("The service was amazing", "positive"),
        Example("I love my family", "positive"),
        Example("They don't care about me", "negative"),
        Example("I hate this place", "negative"),
        Example("The most ridiculous thing I've ever heard", "negative"),
        Example("I am really frustrated", "negative"),
        Example("This is so unfair", "negative"),
        Example("This made me think", "neutral"),
        Example("The good old days", "neutral"),
        Example("What's the difference", "neutral"),
        Example("You can't ignore this", "neutral"),
        Example("That's how I see it", "neutral"),
    ]

    classifications = co.classify(model=model, inputs=input, examples=examples)

    return (
        "Provided sentence is: "
        + ("".join(classifications[0].predictions)).capitalize()
    )
