import io
import streamlit as st
import PyPDF2

from rag_chain import build_prompt
from llm_client import generate_response
from embed_client import get_embeddings
from vector_store import add_to_vectorstore
from utils import chunk_text

# Streamlit UI setup
st.title("🧠 NVIDIA Chat Agent")
st.caption("Powered by NVIDIA NIM, ChromaDB, and Streamlit")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for uploading MULTIPLE files (TXT + PDF)
st.sidebar.title("📄 Upload Files")
uploaded_files = st.sidebar.file_uploader(
    "Choose one or more files",
    type=["txt", "pdf"],
    accept_multiple_files=True
)

# Handle file uploads and indexing
if uploaded_files:
    for uploaded_file in uploaded_files:
        filename = uploaded_file.name.lower()

        # Read TXT
        if filename.endswith(".txt"):
            raw_text = uploaded_file.read().decode("utf-8", errors="ignore")

        # Read PDF
        elif filename.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
            raw_text = ""
            for page in pdf_reader.pages:
                text = page.extract_text()
                if text:
                    raw_text += text + "\n"

        else:
            continue

        if raw_text.strip():
            chunks = chunk_text(raw_text, max_tokens=300)
            embeddings = get_embeddings(chunks)
            add_to_vectorstore(chunks, embeddings)

    st.sidebar.success("All files uploaded and added to vector store.")

# Handle user input
query = st.chat_input("Ask me anything...")
if query:
    prompt = build_prompt(query)
    response = generate_response(prompt, st.session_state.chat_history)

    # Store history
    st.session_state.chat_history.append({"role": "user", "content": query})
    st.session_state.chat_history.append({"role": "assistant", "content": response})

# Render chat messages
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
