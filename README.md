# AI Assistant for Data Science 🤖

## Overview

This Streamlit web application serves as an AI Assistant for Data Science projects. It guides users through the initial steps of data analysis and exploration, providing insights and recommendations based on user-uploaded CSV files. The assistant leverages natural language processing models, including Google's Language Model (GooglePalm), to interactively assist users in their data science journey.

## Features

- **Exploratory Data Analysis (EDA):** The application facilitates EDA by analyzing and summarizing the user's dataset. It covers data cleaning, summarization, correlation analysis, outlier detection, and feature creation.

- **ChatBox:** Users can engage with the AI Assistant in a conversational manner. The ChatBox allows users to ask questions, seek insights about specific variables, and receive recommendations for algorithms suitable for their business problems.

## Getting Started

To run the AI Assistant locally, follow these steps:

1. Clone the repository:

```bash
   git clone https://github.com/RRitika123/AIChatbot 
   cd your-repository
```

2. Install the required dependencies:
```bash
    pip install -r requirements.txt
```

3. Create a .env file in the project root directory and add your Google API key:
```bash
    GOOGLE_API_KEY=your-google-api-key
```

4. Run the streamlit application:
```bash
    streamlit run side.py
```


## Dependencies
- streamlit: The web application framework for creating interactive data science dashboards.
- pandas: Used for handling and manipulating data in DataFrames.
- langchain: A library for natural language processing, including agents, prompts, and chains.
- dotenv: For loading environment variables from a .env file.

## Concepts used

### 1. streamlit

[Streamlit](https://docs.streamlit.io/get-started/fundamentals/main-concepts) is a popular Python library for creating web applications with minimal effort. It is especially well-suited for building interactive data science dashboards.

### 2. Pandas

[Pandas](https://pandas.pydata.org/docs/user_guide/10min.html) is a powerful data manipulation library for Python. It provides data structures like DataFrames, making it easy to handle and analyze tabular data.

### 3. Langchain

[Langchain](https://python.langchain.com/docs/get_started/introduction) is a natural language processing library that includes agents, prompts, and chains. It facilitates interaction with language models and enhances the conversational capabilities of the AI Assistant.

#### Components of Langchain:

- **LLMs:** A large language model (LLM) is a specialized type of artificial intelligence (AI) that has been trained on vast amounts of text to understand existing content and generate original content.
LLM used in our project is GooglePalm

- **Chat models:** ChatGooglePalm

- **Agents:** The application uses Langchain agents to facilitate communication with the GooglePalm language model, allowing for natural language understanding and response generation.

    - **create_pandas_dataframe_agent:** use this agent to interact with a Pandas DataFrame. This agent calls the Python agent under the hood, which executes LLM generated Python code.

- **Prompts:** Langchain prompts are employed to structure and format user queries and prompts for the language model.

    - **PromptTemplate:** 

- **Chains:** Chains allow us to combine multiple components together to create a single, coherent application. For example, we can create a chain that takes user input, formats it with a PromptTemplate, and then passes the formatted response to an LLM. We can build more complex chains by combining multiple chains together, or by combining chains with other components.

    - **LLMChain:** The LLMChain is most basic building block chain. It takes in a prompt template, formats it with the user input and returns the response from an LLM.
    - **SimpleSequentialChain:** The simplest form of sequential chains, where each step has a singular input/output, and the output of one step is the input to the next.
    - **SequentialChain:** A more general form of sequential chains, allowing for multiple inputs/outputs.

- **Document loaders:** 

- **Vector Stores:** One of the most common ways to store and search over unstructured data is to embed it and store the resulting embedding vectors, and then at query time to embed the unstructured query and retrieve the embedding vectors that are 'most similar' to the embedded query. A vector store takes care of storing embedded data and performing vector search for you.

Used chromadb in our project

### 4. Google's Language Model (GooglePalm)

[GooglePalm](https://ai.google.dev/palm_docs/text_quickstart) is a language model developed by Google Research. It is used for natural language understanding in this AI Assistant, providing capabilities for generating responses and insights based on user input.

### 5. dotenv

[python-dotenv](https://pypi.org/project/python-dotenv/) is a Python library that helps in loading environment variables from a `.env` file. It is used in this project to securely manage sensitive information, such as API keys.

## Usage
1. Launch the application and click on the Let's get started button.
![Alt text](<Screenshot 2024-01-03 133651.png>)

2. navigate to the "Data Analysis" tab.
![Alt text](<Screenshot 2024-01-03 133704.png>)

3. Upload a CSV file using the file uploader.

4. Follow the guided EDA steps provided by the AI Assistant.
![Alt text](<Screenshot 2024-01-03 133753.png>)

5. Ask details about any specific variable.
![Alt text](<Screenshot 2024-01-03 134108.png>)

6. Ask the business problem to get the model recommendation.
![Alt text](<Screenshot 2024-01-03 134255.png>)

7. Engage with the ChatBox to ask questions.


## Acknowledgments

- The AI Assistant utilizes Google's Palm Language Model for natural language understanding.
