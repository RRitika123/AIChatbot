import os
import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader

from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.llms import GooglePalm
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain


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



# Initialize the key in session state
if 'clicked' not in st.session_state:
    st.session_state.clicked = {1: False}

# Function to update a value in session state
def clicked(button):
    st.session_state.clicked[button] = True


st.button("Let's get started", on_click=clicked, args=[1])
if st.session_state.clicked[1]:
    tab1, tab2 = st.tabs(["Data Analysis", "ChatBox"])
    with tab1:
        st.header("Exploratory Data Analysis")
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
                st.write(''' - Data Overview''')
                st.write("The first rows of your dataset look like this:")
                st.write(df.head())
                st.markdown("<hr style='margin-top: 20px; margin-bottom: 20px;'>", unsafe_allow_html=True)
                st.subheader("**Data Cleaning**")
                st.write('''- Meaning of the columns:''')
                columns_df = pandas_agent.run("What are the meaning of the columns? Explain them.")
                st.write(columns_df)
                st.write('''- Missing values in the Data:''')
                missing_values = pandas_agent.run("How many missing values does this dataframe have? Start the answer with 'There are'")
                st.write(missing_values)
                st.write('''- Are there any duplicate values?''')
                duplicates = pandas_agent.run("Are there any duplicate values and if so where?")
                st.write(duplicates)
                st.write('''- Data Summarisation''')
                st.write(df.describe())
                st.write('''- Correlation between numerical variables:''')
                correlation_analysis = pandas_agent.run("Calculate correlations between numerical variables to identify potential relationships. If there are no two numerical variable then return No two numerical variables ")
                st.write(correlation_analysis)
                #outliers = pandas_agent.run("Identify outliers in the data that may be erroneous or that may have a significant impact on the analysis.")
                #st.write(outliers)
                st.write('''- What New features can be added ?''')
                new_features = pandas_agent.run("What new features would be interesting to create? Please mention only the name of the new variable.")
                st.write(new_features)
                return
            
            @st.cache_data
            def function_question_variable():
                st.line_chart(df, y =[user_question_variable])
                st.write('''- Summary:''')
                summary_statistics = pandas_agent.run(f"Give me a summary of the statistics of {user_question_variable} in a table format please.")
                st.write(summary_statistics)
                #outliers = pandas_agent.run(f"Assess the presence of outliers of {user_question_variable}")
                #st.write(outliers)
                #trends = pandas_agent.run(f"Analyse trends, seasonality, and cyclic patterns of {user_question_variable}")
                #st.write(trends)
                st.write('''- Missing values for the interested variable is:''')
                missing_values = pandas_agent.run(f"Determine the extent of missing values of {user_question_variable}.")
                st.write(missing_values)
                return
            
            @st.cache_data
            def function_question_dataframe():
                dataframe_info = pandas_agent.run(user_question_dataframe)
                st.write(dataframe_info)
                return    

            #Main
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
                
                    st.divider()

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
                            with st.spinner("Generating response..."):
                                response = chain({'business_problem':prompt})
                                st.write(response["data_problem"])
                                st.write(response["model_selection"])
                        else:
                            st.warning("Please enter a prompt.")

    with tab2:
        st.title("ChatBox")
        st.write("talk with your dataScience book here!")
        pdf = st.file_uploader("Upload your book in pdf form", type="pdf")
        if pdf is not None:
            st.write(pdf)
            pdf_obj = PdfReader(pdf)
            for page in pdf_obj.pages[:3]:
                


