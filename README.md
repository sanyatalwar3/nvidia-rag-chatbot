# NVIDIA RAG Chatbot  
### Workshop: Build Your First AI Chatbot: RAG with NVIDIA  
**Organized by: ACM-W**

This project is a simple **Retrieval-Augmented Generation (RAG)** based AI chatbot built using **Streamlit, ChromaDB, and NVIDIA NIM**.  
The chatbot allows users to upload their own documents and ask questions directly from those documents using AI.

This project was created for the ACM-W workshop:  
**Build Your First AI Chatbot: RAG with NVIDIA**

---

## What This Project Does

- Upload TXT or PDF documents  
- Split documents into smaller chunks  
- Convert chunks into embeddings using NVIDIA AI  
- Store embeddings in a vector database using ChromaDB  
- Retrieve relevant chunks for each user question  
- Generate accurate answers using a Large Language Model  
- Maintain chat history during the session  

---

## Tech Stack Used

- Python  
- Streamlit  
- ChromaDB  
- NVIDIA NIM  
- Requests  
- PyPDF2  

---

## Requirements

- Python 3.8+  
- Streamlit  
- ChromaDB  
- NVIDIA NIM  
- Requests  
- PyPDF2  

To install the requirements, run:

```bash
pip install -r requirements.txt

How to Run This Project
Step 1: Clone the Repository
git clone <PASTE YOUR GITHUB REPO LINK HERE>
cd <YOUR REPO FOLDER NAME>

Step 2: Install Dependencies
pip install -r requirements.txt

Step 3: Create a .env File
touch .env


Add this line inside .env:

NVIDIA_API_KEY=nvapi-xxxxxxxxxxxx

Step 4: Run the Application
streamlit run main.py

Important Notes for Students

The vector database is created locally on your system

You can upload multiple files and the chatbot will answer using all of them

To reset everything, delete the chroma folder or use the clear option if available

About RAG

RAG (Retrieval-Augmented Generation) combines document retrieval with text generation so that the AI answers using real documents instead of guessing.
This allows more accurate answers, reduced hallucinations, and support for private documents.

Powered By

NVIDIA NIM

ChromaDB

Streamlit

License

This project is for educational and ACM-W workshop use only. 
