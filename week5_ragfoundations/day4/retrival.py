import pickle

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

FAISS_INDEX_PATH = BASE_DIR.parent / "day4" / "vector_store.faiss"
METADATA_PATH = BASE_DIR.parent / "day4" / "metadata.pkl"

TOP_K = 5


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index(str(FAISS_INDEX_PATH))

with open(METADATA_PATH, "rb") as f:
    metadata = pickle.load(f)


def retrieve(query: str, top_k: int = TOP_K):

    # Convert question into an embedding
    query_embedding = embedding_model.encode(
        query,
        convert_to_numpy=True
    ).astype("float32")

    # FAISS expects shape (1, embedding_dimension)
    query_embedding = np.expand_dims(query_embedding, axis=0)

    # Search the vector database
    distances, indices = index.search(query_embedding, top_k)

    results = []

    # Convert FAISS indices into actual chunks
    for rank, idx in enumerate(indices[0]):

        if idx == -1:
            continue

        chunk = metadata[idx]

        results.append({
            "rank": rank + 1,
            "distance": float(distances[0][rank]),
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            "text": chunk["text"]
        })

    return results


if __name__ == "__main__":

    question = input("Ask a question: ")

    retrieved_chunks = retrieve(question)

    print("\nRetrieved Chunks")
    print("=" * 60)

    for chunk in retrieved_chunks:

        print(f"\nRank      : {chunk['rank']}")
        print(f"Source    : {chunk['source']}")
        print(f"Chunk ID  : {chunk['chunk_id']}")
        print(f"Distance  : {chunk['distance']:.4f}")
        print("-" * 60)
        print(chunk["text"][:400])