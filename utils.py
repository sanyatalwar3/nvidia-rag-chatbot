# utils.py

def chunk_text(text: str, max_tokens: int = 300):
    """
    Split a long text into smaller chunks (roughly by word count).

    This is a simple approach:
    - Split text into lines
    - Accumulate lines until we reach ~max_tokens words
    - Start a new chunk

    In real systems you might use a tokenizer (e.g. tiktoken),
    but this is good enough for our workshop.
    """
    lines = text.split("\n")
    chunks = []
    current_chunk = []
    current_tokens = 0

    for line in lines:
        if not line.strip():
            continue  # skip blank lines

        tokens = len(line.split())
        # If adding this line would exceed max_tokens, start a new chunk
        if current_tokens + tokens > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [line]
            current_tokens = tokens
        else:
            current_chunk.append(line)
            current_tokens += tokens

    # Add final chunk if present
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks
