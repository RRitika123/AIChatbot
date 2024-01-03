import os
import streamlit as st
import pandas as pd

from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.llms import GooglePalm
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool 


load_dotenv()

st.title("AI Assistant for Data Science 🤖")

st.write("Hello I am your AI Assistant. And I am here to help you with DataScience projects")
with st.sidebar:
    st.write('*Your Data Science project starts with a excel file.*')
    st.caption('''**You may already know that every exciting data science journey starts with a dataset.
    That's why I'd love for you to upload a CSV file.
    Once we have your data in hand, we'll dive into understanding it and have some fun exploring it.
    Then, we'll work together to shape your business challenge into a data science framework.
    I'll introduce you to the coolest machine learning models, and we'll use them to tackle your problem. Sounds fun right?**
    ''')
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
    tab1, tab2 = st.tabs(["Data Analysis and Data science", "ChatBox"])
    with tab1:
        st.header("Exploratory Data Analysis Part")
        st.subheader("Solution")
        user_csv = st.file_uploader("Upload your csv file here", type= "csv")

        if user_csv is not None:
            user_csv.seek(0)
            df = pd.read_csv(user_csv, low_memory=False)

            llm = GooglePalm(google_api_key= os.getenv('GOOGLE_API_KEY'), temperature = 0.2)

            #Function sidebar
            @st.cache_data
            def steps_eda():
                steps_eda = llm('What are the steps of EDA')
                return steps_eda

            pandas_agent = create_pandas_dataframe_agent(llm= llm, df =df, verbose=True)
            
            @st.cache_data
            def function_agent():
                st.write("**Data Overview**")
                st.write("The first rows of your dataset look like this:")
                st.write(df.head())
                st.write("**Data Cleaning**")
                columns_df = pandas_agent.run("What are the meaning of the columns?")
                st.write(columns_df)
                missing_values = pandas_agent.run("How many missing values does this dataframe have? Start the answer with 'There are'")
                st.write(missing_values)
                duplicates = pandas_agent.run("Are there any duplicate values and if so where?")
                st.write(duplicates)
                st.write("**Data Summarisation**")
                st.write(df.describe())
                correlation_analysis = pandas_agent.run("Calculate correlations between numerical variables to identify potential relationships.")
                st.write(correlation_analysis)
                outliers = pandas_agent.run("Identify outliers in the data that may be erroneous or that may have a significant impact on the analysis.")
                st.write(outliers)
                new_features = pandas_agent.run("What new features would be interesting to create?.")
                st.write(new_features)
                return
            
            @st.cache_data
            def function_question_variable():
                st.line_chart(df, y =[user_question_variable])
                summary_statistics = pandas_agent.run(f"Give me a summary of the statistics of {user_question_variable}")
                st.write(summary_statistics)
                outliers = pandas_agent.run(f"Assess the presence of outliers of {user_question_variable}")
                st.write(outliers)
                trends = pandas_agent.run(f"Analyse trends, seasonality, and cyclic patterns of {user_question_variable}")
                st.write(trends)
                missing_values = pandas_agent.run(f"Determine the extent of missing values of {user_question_variable}")
                st.write(missing_values)
                return
            
            @st.cache_data
            def function_question_dataframe():
                dataframe_info = pandas_agent.run(user_question_dataframe)
                st.write(dataframe_info)
                return    

            #Main
            st.header('Exploratory data analysis')
            st.subheader('General information about the dataset')

            with st.sidebar:
                with st.expander('What are the steps of EDA'):
                    st.write(steps_eda())

            function_agent()

            st.subheader('Variable of study')
            user_question_variable = st.text_input('What variable are you interested in')
            if user_question_variable is not None and user_question_variable !="":
                function_question_variable()

                st.subheader('Further study')

            if user_question_variable:
                user_question_dataframe = st.text_input( "Is there anything else you would like to know about your dataframe?")
                if user_question_dataframe is not None and user_question_dataframe not in ("","no","No"):
                    function_question_dataframe()
                if user_question_dataframe in ("no", "No"):
                    st.write("")       

                    if user_question_dataframe:
                        st.divider()
                        st.header("DataScience Problem")
                        st.write("Now that we have a solid grasp of the data")
                        
                        prompt = st.text_area("What is the business problem that you want to solve?")

                        problem_template = PromptTemplate(
                            input_variables=["business_problem"],
                            template="Convert the following business problem into a data science problem: {business_problem}"
                        )

                        model_template = PromptTemplate(
                            input_variables=["data_problem"],
                            template="Give a list of algorithms that are suitable for the problem: {data_problem}."
                        )
                        problem_chain = LLMChain(llm=llm, prompt = problem_template, verbose=True, output_key="data_problem")
                        model_chain = LLMChain(llm=llm, prompt =  model_template, verbose=True, output_key="model_selection")
                        chain = SequentialChain(chains=[problem_chain, model_chain], input_variables=["business_problem"], output_variables=["data_problem","model_selection"], verbose=True)           
            

                        if prompt:
                            response = chain({'business_problem':prompt})
                            st.write(response["data_problem"])
                            st.write(response["model_selection"])

    with tab2:
        st.header("ChatBox")
        st.write("Welcome to the AI Assistant ChatBox!")
        st.write("")
