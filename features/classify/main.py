import streamlit as st
import cohere
from cohere import ClassifyExample


@st.cache_data
def classify_content(key, inputs):
    co = cohere.Client(key)
    examples = [
        ClassifyExample(text="I'm so proud of you", label="positive"),
        ClassifyExample(text="What a great time to be alive", label="positive"),
        ClassifyExample(text="That's awesome work", label="positive"),
        ClassifyExample(text="The service was amazing", label="positive"),
        ClassifyExample(text="I love my family", label="positive"),
        ClassifyExample(text="They don't care about me", label="negative"),
        ClassifyExample(text="I hate this place", label="negative"),
        ClassifyExample(text="The most ridiculous thing I've ever heard", label="negative"),
        ClassifyExample(text="I am really frustrated", label="negative"),
        ClassifyExample(text="This is so unfair", label="negative"),
        ClassifyExample(text="This made me think", label="neutral"),
        ClassifyExample(text="The good old days", label="neutral"),
        ClassifyExample(text="What's the difference", label="neutral"),
        ClassifyExample(text="You can't ignore this", label="neutral"),
        ClassifyExample(text="That's how I see it", label="neutral"),
    ]

    classifications = co.classify(inputs=inputs, examples=examples)

    return (
        "Provided sentence is: "
        + classifications.classifications[0].prediction.capitalize()
    )
