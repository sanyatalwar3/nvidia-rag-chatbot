# rag_chain.py
from embed_client import get_embeddings
from vector_store import query_vectorstore


def build_prompt(query: str) -> str:
    """
    Build the final prompt we send to the LLM.

    Steps:
    1. Embed the user's question
    2. Retrieve similar document chunks from ChromaDB
    3. Combine context + question into a single prompt string
    """
    # 1) Embed the query
    query_embedding = get_embeddings([query])[0]

    # 2) Get top-k similar chunks
    retrieved_docs = query_vectorstore(query_embedding)

    # 3) Join them into a context section
    context = "\n".join(retrieved_docs)

    # 4) Build the prompt
    prompt = (
        "You are a helpful assistant. Use the context below to answer the question.\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{query}"
    )

    return prompt
