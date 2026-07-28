from pathlib import Path
import pickle
from rank_bm25 import BM25Okapi
from collections import defaultdict


BASE_DIR = Path(__file__).resolve().parent

METADATA_PATH = (
    BASE_DIR.parent.parent
    / "week5_ragfoundations"
    / "day4"
    / "metadata.pkl"
)
with open(METADATA_PATH, "rb") as f:
    metadata = pickle.load(f)

# print(metadata)

documents = [
    item["text"]
    for item in metadata
]


print(documents)


tokenized_docs = [
    doc.lower().split()
    for doc in documents
]


bm25 = BM25Okapi(tokenized_docs)

query = input("Enter your query: ")

tokenized_query = query.lower().split()

results = bm25.get_top_n(
    tokenized_query,
    documents,
    n=5
)

for i, result in enumerate(results, 1):
    print(f"\nResult {i}")
    print(result)
    

sorted_res = defaultdict(float)

for rank,doc in enumerate(results):
    sorted_res[doc] +=1/(60+rank+1)

final_results = sorted(
    sorted_res.items(),
    key=lambda x: x[1],
    reverse=True
)

print(final_results)