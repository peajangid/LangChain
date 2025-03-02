from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

import os 
from dotenv import load_dotenv

load_dotenv()
##here we wil be using ollama gemma2 model so for that run ollama run gemma to download the complete mode

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('Langchain Demo With gemma API')
input_text=st.text_input("Search the topic u want")

# ollama gemma LLm 
llm=Ollama(model="gemma")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))


## TO RUN JUST WRITE STREAMLIT RUN LOCAL_LLAMA.PY
