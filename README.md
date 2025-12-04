project:
  name: NVIDIA RAG Chatbot
  workshop_title: "Build Your First AI Chatbot: RAG with NVIDIA"
  organized_by: "ACM-W"

description: >
  This project is a simple Retrieval-Augmented Generation (RAG) based AI chatbot
  built using Streamlit, ChromaDB, and NVIDIA NIM. The chatbot allows users to
  upload their own documents and ask questions directly from those documents
  using AI. This project is created for the ACM-W workshop: Build Your First AI
  Chatbot: RAG with NVIDIA.

features:
  - Upload TXT or PDF documents
  - Split documents into smaller chunks
  - Convert chunks into embeddings using NVIDIA AI
  - Store embeddings in a vector database using ChromaDB
  - Retrieve relevant chunks for each user question
  - Generate accurate answers using a large language model
  - Maintain chat history during the session

tech_stack:
  - Python
  - Streamlit
  - ChromaDB
  - NVIDIA NIM
  - Requests
  - PyPDF2

how_to_run:
  step_1_clone:
    description: "Clone the repository"
    commands:
      - git clone <PASTE YOUR GITHUB REPO LINK HERE>
      - cd <YOUR REPO FOLDER NAME>

  step_2_install:
    description: "Install dependencies"
    commands:
      - pip install -r requirements.txt

  step_3_env:
    description: "Create a .env file and add the API key"
    commands:
      - touch .env
      - NVIDIA_API_KEY=nvapi-xxxxxxxxxxxx

  step_4_run:
    description: "Run the application"
    commands:
      - streamlit run main.py

important_notes:
  - The vector database is created locally on your system
  - You can upload multiple files and the chatbot will answer using all of them
  - To reset everything, delete the chroma folder or use the clear option if available

about_rag: >
  RAG (Retrieval-Augmented Generation) combines document retrieval with text
  generation so that the AI answers using real documents instead of guessing.
  This allows more accurate answers, reduced hallucinations, and support for
  private documents.

powered_by:
  - NVIDIA NIM
  - ChromaDB
  - Streamlit

license: "This project is for educational and ACM-W workshop use only."
