import os
import streamlit as st
from secret import openai_key
import pandas as pd

from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv

#load_dotenv()  # Load variables from .env file

#api_key = os.getenv("API_KEY")

os.environ['OPENAI_API_KEY'] = openai_key
load_dotenv(find_dotenv())
llm = OpenAI(temperature=0)

st.title("AI Assistant for Data Science 🤖")

st.write("Hello I am your AI Assistant. And I am here to help you with DataScience projects")
with st.sidebar:
    st.write('*Your Data Science project starts with a excel file.*')
    st.caption('''**You may already know that every exciting data science journey starts with a dataset. That's why I'd love for you to upload a CSV file. Once we have your data in hand, we'll dive into understanding it and have some fun exploring it. Then, we'll work together to shape your business challenge into a data science framework. I'll introduce you to the coolest machine learning models, and we'll use them to tackle your problem. Sounds fun right?**''')
    st.divider()
    st.caption("<p style='text-align:center'> by Ritika</p>", unsafe_allow_html=True)



# Initialize the key in session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = {1: False}

# Function to update a value in session state
def clicked(button):
    st.session_state.clicked[button] = True
st.button("Let's get started", on_click=clicked, args=[1])
if st.session_state.clicked[1]:
    st.header("Exploratory Data Analysis Part")
    st.subheader("Solution")
    user_csv = st.file_uploader("Upload your csv file here", type= "csv")

    if user_csv is not None:
        user_csv.seek(0)
        df = pd.read_csv(user_csv, low_memory=False)

#steps_eda = llm("What steps are involved in EDA?")
with st.sidebar:
    with st.expander("What are the steps of EDA ?"):
        st.caption(llm("What are steps of EDA ?"))
