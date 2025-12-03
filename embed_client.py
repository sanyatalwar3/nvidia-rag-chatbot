# embed_client.py
import os
import requests
from dotenv import load_dotenv

# Load NVIDIA_API_KEY from .env file
load_dotenv()
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

BASE = "https://integrate.api.nvidia.com/v1"

# Authentication headers for NVIDIA API
HEADERS = {
    "Authorization": f"Bearer {NVIDIA_API_KEY}",
    "Content-Type": "application/json",
}

# NVIDIA text embedding model hosted on NIM
MODEL_EMBED = "nvidia/nv-embedqa-e5-v5"


def get_embeddings(texts):
    """
    Convert one or more pieces of text into vector embeddings.

    texts: list[str]
        - For documents: list of chunks (input_type = "passage")
        - For user queries: list with a single string (input_type can be "query")
    """
    payload = {
        "model": MODEL_EMBED,
        "input": texts,
        # "passage" = document text we want to store in the vector DB
        # "query"   = user question text
        "input_type": "passage",
    }

    # Call NVIDIA embeddings endpoint
    r = requests.post(f"{BASE}/embeddings", headers=HEADERS, json=payload)

    if r.status_code != 200:
        raise Exception(f"{r.status_code} {r.text}")

    data = r.json()

    # Return list of embedding vectors (one per input text)
    return [item["embedding"] for item in data["data"]]
