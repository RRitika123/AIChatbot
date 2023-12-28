import os
import streamlit as st
from secret import openai_key
import pandas as pd

from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv

#load_dotenv()  # Load variables from .env file

#api_key = os.getenv("API_KEY")

st.title("AI Assistant for Data Science")
st.header("Exploratory Data Analysis Part")
st.subheader("Solution")
st.write("Hello I am your AI Assistant. And I am here to help you with DataScience projects")
with st.sidebar:
    st.write('Your Data Science project starts with a excel file.')
    st.caption('''So let us get your excel file and start working.''')