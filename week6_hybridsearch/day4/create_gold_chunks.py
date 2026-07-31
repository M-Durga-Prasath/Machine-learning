import argparse
import json
import os
import pickle
import re
from pathlib import Path

import faiss
import numpy as np
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer


BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parents[1]
WEEK5_DAY4 = PROJECT_ROOT / "week5_ragfoundations" / "day4"

QA_PATH = BASE_DIR / "qa.json"
METADATA_PATH = WEEK5_DAY4 / "metadata.pkl"
FAISS_INDEX_PATH = WEEK5_DAY4 / "vector_store.faiss"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"
GROQ_MODEL = "llama-3.3-70b-versatile"


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.write("\n")


def load_metadata(path):
    with open(path, "rb") as file:
        return pickle.load(file)


def retrieve_candidates(question, embedding_model, index, metadata, top_k):
    query_embedding = embedding_model.encode(
        question,
        convert_to_numpy=True,
    ).astype("float32")

    query_embedding = np.expand_dims(query_embedding, axis=0)
    distances, indices = index.search(query_embedding, top_k)

    candidates = []
    for rank, idx in enumerate(indices[0], start=1):
        if idx == -1:
            continue

        chunk = metadata[idx]
        candidates.append(
            {
                "candidate_id": len(candidates),
                "rank": rank,
                "distance": float(distances[0][rank - 1]),
                "source": chunk["source"],
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"],
            }
        )

    return candidates


def trim_text(text, limit):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0] + "..."


def build_label_prompt(qa, candidates, text_limit):
    candidate_text = []

    for candidate in candidates:
        candidate_text.append(
            "\n".join(
                [
                    f"candidate_id: {candidate['candidate_id']}",
                    f"source: {candidate['source']}",
                    f"chunk_id: {candidate['chunk_id']}",
                    f"text: {trim_text(candidate['text'], text_limit)}",
                ]
            )
        )

    return f"""
You are labeling retrieval evaluation data.

Choose the chunk or chunks that contain the evidence needed to answer the question.
Use only the candidate chunks below.
If none of the candidate chunks contain the answer, return an empty list.

Return only valid JSON in this exact format:
{{
  "gold_chunks": [
    {{"source": "file.pdf", "chunk_id": 123}}
  ]
}}

Question:
{qa["question"]}

Gold answer:
{qa.get("gold_answer", "")}

Candidate chunks:
{"\n\n---\n\n".join(candidate_text)}
""".strip()


def extract_json(text):
    text = text.strip()

    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()

    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end < start:
        raise ValueError(f"Groq did not return JSON: {text}")

    return json.loads(text[start : end + 1])


def choose_gold_chunks(client, qa, candidates, text_limit):
    prompt = build_label_prompt(qa, candidates, text_limit)

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        response_format={"type": "json_object"},
    )

    parsed = extract_json(response.choices[0].message.content)
    gold_chunks = parsed.get("gold_chunks", [])

    allowed = {
        (candidate["source"], candidate["chunk_id"])
        for candidate in candidates
    }

    clean_gold_chunks = []
    seen = set()

    for chunk in gold_chunks:
        source = chunk.get("source")
        chunk_id = chunk.get("chunk_id")
        key = (source, chunk_id)

        if key not in allowed or key in seen:
            continue

        clean_gold_chunks.append(
            {
                "source": source,
                "chunk_id": chunk_id,
            }
        )
        seen.add(key)

    return clean_gold_chunks


def label_qa_file(args):
    load_dotenv(BASE_DIR / ".env")
    load_dotenv(WEEK5_DAY4 / ".env")

    if not os.getenv("GROQ_API_KEY"):
        raise RuntimeError("GROQ_API_KEY was not found in .env or environment variables.")

    qa_pairs = load_json(args.qa_path)
    metadata = load_metadata(args.metadata_path)
    index = faiss.read_index(str(args.faiss_path))
    embedding_model = SentenceTransformer(EMBEDDING_MODEL)
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    labeled = []

    if args.in_place:
        backup_path = args.qa_path.with_suffix(".backup.json")
        save_json(backup_path, qa_pairs)
        target_path = args.qa_path
    else:
        backup_path = None
        target_path = args.output

    for number, qa in enumerate(qa_pairs, start=1):
        print(f"[{number}/{len(qa_pairs)}] {qa['question']}")

        candidates = retrieve_candidates(
            qa["question"],
            embedding_model,
            index,
            metadata,
            args.candidates,
        )

        updated_qa = dict(qa)
        updated_qa["gold_chunks"] = choose_gold_chunks(
            client,
            qa,
            candidates,
            args.text_limit,
        )

        labeled.append(updated_qa)
        print(f"  gold_chunks: {updated_qa['gold_chunks']}")

        save_json(target_path, labeled + qa_pairs[number:])

    if args.in_place:
        print(f"\nUpdated {args.qa_path}")
        print(f"Backup saved to {backup_path}")
    else:
        print(f"\nSaved labeled QA file to {args.output}")


def parse_args():
    parser = argparse.ArgumentParser(
        description="Use Groq to replace qa.json gold_chunks with matching source/chunk_id evidence."
    )
    parser.add_argument("--qa-path", type=Path, default=QA_PATH)
    parser.add_argument("--metadata-path", type=Path, default=METADATA_PATH)
    parser.add_argument("--faiss-path", type=Path, default=FAISS_INDEX_PATH)
    parser.add_argument("--output", type=Path, default=BASE_DIR / "qa_labeled.json")
    parser.add_argument("--candidates", type=int, default=30)
    parser.add_argument("--text-limit", type=int, default=900)
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Overwrite qa.json and save the original as qa.backup.json.",
    )
    return parser.parse_args()


if __name__ == "__main__":
    label_qa_file(parse_args())
