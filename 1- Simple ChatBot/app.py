from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv
# Langsmith Tracking
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
# or we can use this -> load_dotenv()

# prompt template 
template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful chat assistant tha answers every query the user asks'), 
    ('user', 'Question: {question}')
])

# Chat Model
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash', temperature=0)

# Output Parser
output_parser = StrOutputParser()

# Chain
chain = template | model | output_parser

# streamlit app
st.title('Q&A Chat with Gemini')
input_text = st.text_input("Ask whatever you want and I will try to help!")

if input_text:
    output = chain.stream({'question': input_text})
    for chunk in output:
        st.write(chunk)