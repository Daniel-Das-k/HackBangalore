# SME Financial Inclusion 

## Overview
The SME Financial Inclusion Project aims to enhance the accessibility of financial services for Small and Medium Enterprises (SMEs). This repository features two key components:

Credit Score Prediction System: An intelligent model designed to predict the credit scores of SMEs based on financial data, facilitating better decision-making for financial institutions and SMEs.
SME Information Chatbot: An advanced chatbot that provides detailed information on SME-related queries, leveraging the power of natural language processing and online resources.

## Features
* Credit Score Prediction: Helps financial institutions assess the creditworthiness of SMEs by analyzing their financial metrics.
* Information Retrieval: The chatbot assists users by fetching and delivering information on SME policies, loan processes, and more, making it easier for SMEs to navigate financial services.
* Scalable and Extensible: The project is built to be scalable, with potential for integration with other financial tools and services.

## How This Project Helps 
### For Financial Institutions
* Efficient Risk Assessment: By predicting credit scores, institutions can streamline the loan approval process and reduce the risk of defaults.
* Data-Driven Decisions: Enables the use of clustering and predictive analytics to make informed lending decisions.
### For SMEs
* Access to Information: The chatbot provides SMEs with quick answers to their questions about financing, loans, and banking services.
* Improved Financial Management: SMEs can understand their credit positions better and manage their financial health more effectively.

## Technologies Used
* Python: The core programming language for developing the machine learning model and chatbot functionalities.
* Scikit-Learn: Used for clustering and predictive analytics in the credit score prediction system.
* Joblib: Utilized for model serialization and deserialization, allowing easy saving and loading of trained models.
* Langchain: Powers the chatbot, enabling advanced natural language processing and interaction capabilities.
* FAISS: Provides efficient similarity search and clustering for the chatbot’s information retrieval system.
* OpenAI GPT: Enhances the chatbot’s ability to understand and respond to SME-related queries with the help of advanced language models.

## How to Run

To run the SME Financial Inclusion Project locally, follow these steps:

1. **Set Up Conda Environment**:
   ```bash
   conda create -n sme-env python=3.11
   conda activate sme-env
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/Daniel-Das-k/SME-Financial_Inclusion.git
   cd SME-Financial_Inclusion
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Running the Applications:**:
* To Run the Chatbot:
   ```bash
   python chatbot.py
+ To Run the Credit Score Prediction System:
   ```bash
   python creditscore.py

## Usage

### Credit Score Prediction System
The system analyzes financial data to predict credit scores for SMEs, helping financial institutions make better lending decisions.

### SME Information Chatbot
The chatbot uses machine learning to provide SMEs with relevant information by processing queries related to financing, loan applications, and more.
