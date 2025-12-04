# Build Your First AI Chatbot: RAG with NVIDIA  
Organized by: ACM-W  

This repository contains the complete code used in the ACM-W workshop **“Build Your First AI Chatbot: RAG with NVIDIA”**.  
In this workshop, students learn the **basics of Retrieval-Augmented Generation (RAG)** and build a working AI chatbot that can answer questions from their own documents.

---

## Basics of RAG (Retrieval-Augmented Generation)

RAG is a technique that combines **document retrieval** with **text generation**.

Instead of answering only from what a model already knows, a RAG system:
- First searches relevant information from uploaded documents  
- Then uses that information as context to generate accurate answers  

This makes the chatbot:
- More accurate  
- Less likely to hallucinate  
- Able to answer from private PDFs and documents  
- Easy to update without retraining the model  

---

## What This Chatbot Does

- Allows users to upload TXT or PDF documents  
- Splits documents into smaller chunks  
- Converts each chunk into embeddings using NVIDIA AI  
- Stores embeddings in a vector database using ChromaDB  
- Retrieves the most relevant chunks for each question  
- Sends the retrieved context to the LLM  
- Generates grounded answers from the documents  
- Maintains chat history during the session  

---

## Tech Stack

- Python  
- Streamlit  
- ChromaDB  
- NVIDIA NIM  
- Requests  
- PyPDF2  
- python-dotenv  

---

## How to Run the Project

# Clone the GitHub repository
git clone <PASTE YOUR GITHUB REPO LINK HERE>

# Go inside the project folder
cd <YOUR REPO FOLDER NAME>

# Install all required Python packages
pip install -r requirements.txt

# Create a file to store your NVIDIA API key
touch .env

# Add your NVIDIA API key to the .env file
echo "NVIDIA_API_KEY=nvapi-xxxxxxxxxxxxxxxx" > .env

# Run the Streamlit application
streamlit run main.py
