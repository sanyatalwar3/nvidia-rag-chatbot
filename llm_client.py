# llm_client.py
from pathlib import Path
import os
import json
import requests

from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Load .env from project root and current directory
load_dotenv(dotenv_path=(Path(__file__).resolve().parent.parent / ".env"))
load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
if not NVIDIA_API_KEY or not NVIDIA_API_KEY.startswith("nvapi-"):
    raise RuntimeError("NVIDIA_API_KEY missing/invalid in .env")

BASE = "https://integrate.api.nvidia.com/v1"
CHAT_URL = f"{BASE}/chat/completions"

# We will use this chat model from NVIDIA NIM
DEFAULT_MODEL = "mistralai/mistral-7b-instruct-v0.3"

# Headers for JSON responses
HEADERS_JSON = {
    "Authorization": f"Bearer {NVIDIA_API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Headers for streaming responses (Server-Sent Events)
HEADERS_STREAM = {
    "Authorization": f"Bearer {NVIDIA_API_KEY}",
    "Content-Type": "application/json",
    "Accept": "text/event-stream",
}

# Create a session with automatic retries (for reliability)
_session = requests.Session()
_session.mount(
    "https://",
    HTTPAdapter(
        max_retries=Retry(
            total=3,
            connect=3,
            read=3,
            backoff_factor=0.6,          # wait times: 0.6s, 1.2s, 2.4s...
            status_forcelist=[502, 503, 504],
            allowed_methods=["POST"],
        )
    ),
)


def _payload(model, messages, temperature, max_tokens, stream):
    """Small helper to build the JSON payload."""
    return {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": stream,
    }


def generate_response(
    prompt: str,
    history=None,
    model: str = DEFAULT_MODEL,
    temperature: float = 0.4,
    max_tokens: int = 192,
) -> str:
    """
    Send a prompt to NVIDIA NIM chat/completions API and get a final text answer.

    For a smoother UX, we first try streaming.
    If streaming fails, we fall back to a normal (non-streaming) request.
    """

    # Simple chat format: system + user
    messages = [
        {
            "role": "system",
            "content": "Be concise. Use provided context faithfully. If unsure, say so.",
        },
        {"role": "user", "content": prompt},
    ]

    # Try streaming first
    try:
        resp = _session.post(
            CHAT_URL,
            headers=HEADERS_STREAM,
            json=_payload(model, messages, temperature, max_tokens, stream=True),
            timeout=(10, 120),
            stream=True,
        )
        resp.raise_for_status()

        chunks = []
        for line in resp.iter_lines():
            if not line:
                continue

            # Each streaming line starts with "data: "
            if line.startswith(b"data: "):
                data = line[len(b"data: "):].strip()
                if data == b"[DONE]":
                    break

                try:
                    obj = json.loads(data.decode("utf-8"))
                    delta = obj["choices"][0]["delta"].get("content", "")
                    if delta:
                        chunks.append(delta)
                except Exception:
                    # Ignore malformed keepalive events
                    continue

        text = "".join(chunks).strip()
        if text:
            return text

    except requests.exceptions.ReadTimeout:
        # If streaming times out, we will use non-streaming below
        pass

    # Non-streaming fallback
    resp = _session.post(
        CHAT_URL,
        headers=HEADERS_JSON,
        json=_payload(model, messages, temperature, max_tokens, stream=False),
        timeout=(10, 120),
    )

    if resp.status_code != 200:
        raise Exception(f"{resp.status_code} {resp.text}")

    return resp.json()["choices"][0]["message"]["content"]
