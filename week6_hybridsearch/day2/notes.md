1. What is Domain Shift?

Domain shift occurs when the data used in the real world is different from the data on which the retrieval model was trained. As a result, the model may struggle to understand new vocabulary, writing styles, or specialized terminology.

2. Why does Dense Retrieval degrade across domains?

Dense retrieval relies on embeddings learned from training data. When it encounters unfamiliar domains such as legal, medical, or financial documents, the embeddings may not capture the specialized meanings of terms, leading to less accurate retrieval.

Beir - benchmarking information retrival -> A benchmark used to evaluate retrieval systems across many different domains.


RRF (Reciprocal Rank Fusion)
Merges rankings from multiple retrieval methods by rewarding documents that rank well in both.