Build Your First AI Chatbot: RAG with NVIDIA

Organized by: ACM-W

This repository contains the complete code used in the ACM-W workshop “Build Your First AI Chatbot: RAG with NVIDIA”.
In this workshop, students learn the basics of Retrieval-Augmented Generation (RAG) and build a working AI chatbot that can answer questions from their own documents.

Basics of RAG (Retrieval-Augmented Generation)

RAG is a technique that combines document retrieval with text generation.

Instead of answering only from what a model already knows, a RAG system:

First searches relevant information from uploaded documents

Then uses that information as context to generate accurate answers

This makes the chatbot:

More accurate

Less likely to hallucinate

Able to answer from private PDFs and documents

Easy to update without retraining the model

What This Chatbot Does

Allows users to upload TXT or PDF documents

Splits documents into smaller chunks

Converts each chunk into embeddings using NVIDIA AI

Stores embeddings in a vector database using ChromaDB

Retrieves the most relevant chunks for each question

Sends the retrieved context to the LLM

Generates grounded answers from the documents

Maintains chat history during the session

Tech Stack

Python

Streamlit

ChromaDB

NVIDIA NIM

Requests

PyPDF2

python-dotenv

How to Run the Project

Clone the repository:

git clone <PASTE YOUR GITHUB REPO LINK HERE>
cd <YOUR REPO FOLDER NAME>


Install dependencies:

pip install -r requirements.txt


Create a .env file:

touch .env


Add your NVIDIA API key inside .env:

NVIDIA_API_KEY=nvapi-xxxxxxxxxxxxxxxx


Run the application:

streamlit run main.py

Important Notes for Students

The vector database is created locally on your system

You can upload multiple files and the chatbot will use all of them

To reset everything, delete the chroma folder

Do NOT upload your .env file or API key to GitHub

About the Workshop

This project was developed as part of the ACM-W technical workshop
“Build Your First AI Chatbot: RAG with NVIDIA”, where students learned the fundamentals of RAG and built an end-to-end document-based chatbot using NVIDIA models.

License

This project is for educational and ACM-W workshop use only.
