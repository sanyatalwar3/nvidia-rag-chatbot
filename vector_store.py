# vector_store.py
from __future__ import annotations

import os
from pathlib import Path
import uuid
from typing import List, Sequence, Any

import chromadb

# Directory to store the ChromaDB files on disk
DB_PATH = Path(__file__).resolve().parent / "data" / "chroma"
os.makedirs(DB_PATH, exist_ok=True)

# Create Chroma client (persistent if possible)
try:
    client = chromadb.PersistentClient(path=str(DB_PATH))
except AttributeError:
    # Fallback for older chromadb versions
    client = chromadb.Client()

COLLECTION_NAME = "chat_docs"


def _get_collection():
    """Get (or create) the ChromaDB collection used for our RAG app."""
    return client.get_or_create_collection(name=COLLECTION_NAME)


# Start with one collection object
collection = _get_collection()


def _to_list(x: Any) -> list:
    """
    Ensure embedding is a plain Python list.
    Supports numpy arrays / torch tensors / etc.
    """
    if hasattr(x, "tolist"):
        return x.tolist()
    return list(x)


def clear_vectorstore() -> None:
    """
    Delete the existing collection and recreate an empty one.

    Use this if the user wants to 'reset' all uploaded documents.
    """
    global collection

    try:
        client.delete_collection(COLLECTION_NAME)
        print(f"[INFO] Deleted collection '{COLLECTION_NAME}'.")
    except Exception as e:
        print(f"[WARN] Could not delete collection '{COLLECTION_NAME}': {e}")

    collection = _get_collection()
    print(f"[INFO] Recreated empty collection '{COLLECTION_NAME}'.")


def add_to_vectorstore(docs: Sequence[str], embeddings: Sequence[Any]) -> None:
    """
    Add document chunks and their embeddings into ChromaDB.
    """
    if len(docs) != len(embeddings):
        raise ValueError("docs and embeddings must be the same length")

    ids: List[str] = [f"doc_{uuid.uuid4().hex}" for _ in range(len(docs))]
    embeds: List[list] = [_to_list(e) for e in embeddings]

    collection.add(documents=list(docs), embeddings=embeds, ids=ids)


def query_vectorstore(query_embedding: Any, top_k: int = 3) -> List[str]:
    """
    Given a single query embedding, return the top-k most similar documents.
    """
    q_embed = _to_list(query_embedding)
    res = collection.query(query_embeddings=[q_embed], n_results=top_k)
    return res.get("documents", [[]])[0]


def get_doc_count() -> int:
    """Return how many documents are stored (for debugging/UI)."""
    try:
        return collection.count()
    except Exception:
        return -1
