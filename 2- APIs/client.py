import requests 
import streamlit as st


def get_essay_response(input_text):
    response = requests.post(url='http://localhost:8000/essay/invoke', 
                             json={'input': {'topic': input_text}})
    return response.json()["output"]["content"]

def get_poem_response(input_text):
    response = requests.post(url='http://localhost:8000/poem/invoke', 
                             json={'input': {'topic': input_text}})
    return response.json()["output"]["content"]

st.title("Using Multiple Models for Multiple Tasks")
poem_topic = st.text_input("Write a poem about....")
essay_topic = st.text_input("Write an essay about....")

if poem_topic:
    st.write(get_poem_response(poem_topic))

if essay_topic:
    st.write(get_essay_response(essay_topic))

