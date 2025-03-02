from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = os.getenv('LANGCHAIN_TRACING_V2')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

## Propmpt template
prompt = ChatPromptTemplate(
    [
    ('system','please respond to the user queries'),
    ('user','queston": {question}'),
    (' ')
    ]
)

## Streamlit frame work 
st.title('Langchain dummychatbot like chatgpt')
input_text = st.text_input('Search what u want')

# Open AI LLM
llm = ChatOpenAI(model='gpt-3.5-turbo')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))