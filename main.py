import os
import streamlit as st
import pandas as pd

from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
from langchain.llms import OpenAI


from dotenv import load_dotenv, find_dotenv

import google.generativeai as genai
load_dotenv()

llm = OpenAI(openai_api_key= os.environ["OPENAI_API_KEY"] ,temperature = 0)
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

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

# with st.sidebar:
#     with st.expander("What are the steps of EDA ?"):
#         st.caption(model.generate_content("What are steps of EDA ?").text)



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




        st.write("**Data Overview**")
        st.write("The first rows of your dataset looks like this:")
        st.write(df.head())
        st.write(create_pandas_dataframe_agent(llm= model, df =df, verbose=True).run("What are the meanings of the columns??"))
        #st.write(create_pandas_dataframe_agent(llm, df, verbose=True).run("How many missing values are there in this dataset?"))

        # def function_agent():
        #     st.write("**Data cleaning**")
        #     columns_df = pandas_agent.run("What are the meanings of the columns?")
        #     st.write(columns_df)
        #     # missing_values = pandas_agent.run("How many missing values are there in this dataset?")
        #     # st.write(missing_values)
        #     return 

        # function_agent()