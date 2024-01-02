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