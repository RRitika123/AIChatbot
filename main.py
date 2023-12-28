import os
import streamlit as st
from key import openai_key
import pandas as pd

from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv

#load_dotenv()  # Load variables from .env file

#api_key = os.getenv("API_KEY")

st.title("AI Assistant for Data Science")
st.header("Exploratory Data Analysis Part")
st.header("Solution")