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

## Usage
1. Launch the application and navigate to the "Data Analysis and Data Science" tab.

2. Upload a CSV file using the file uploader.

3. Follow the guided EDA steps provided by the AI Assistant.

4. Engage with the ChatBox to ask questions, explore specific variables, and define data science problems.

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

- **Agents:** The application uses Langchain agents to facilitate communication with the GooglePalm language model, allowing for natural language understanding and response generation.

- **Prompts:** Langchain prompts are employed to structure and format user queries and prompts for the language model.

- **Chains:** Langchain chains are utilized to sequence multiple language model interactions, enabling a step-by-step approach in guiding users through exploratory data analysis and problem definition.

- **Tools:** The PythonREPLTool from Langchain is used to integrate a Python REPL (Read-Eval-Print Loop) within the application, enhancing its interactive capabilities.


### 4. Google's Language Model (GooglePalm)

[GooglePalm](https://ai.google.dev/palm_docs/text_quickstart) is a language model developed by Google Research. It is used for natural language understanding in this AI Assistant, providing capabilities for generating responses and insights based on user input.

### 5. dotenv

[python-dotenv](https://pypi.org/project/python-dotenv/) is a Python library that helps in loading environment variables from a `.env` file. It is used in this project to securely manage sensitive information, such as API keys.


## Acknowledgments

- The AI Assistant utilizes Google's Palm Language Model for natural language understanding.
