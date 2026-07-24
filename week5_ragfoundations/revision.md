# Why is CLS pooling worse than Mean Pooling for semantic search?

Because:

BERT's CLS token was trained mainly for classification, not for measuring sentence similarity.

Mean pooling uses information from all tokens, giving a more complete representation of the sentence.

Sentence Transformers were trained with mean pooling specifically so that similar sentences produce similar embeddings.



# Why is cosine similarity preferred over Euclidean distance for semantic search?

Because:

Cosine similarity measures the angle between vectors, focusing on their direction rather than their length.
Sentence embeddings can have different magnitudes even when they represent similar meanings.
Euclidean distance is affected by vector magnitude, so two semantically similar embeddings can appear far apart if one vector is simply scaled.
Cosine similarity ignores magnitude and compares semantic orientation, making it a better measure of meaning.
Most embedding models (e.g., Sentence Transformers) are designed and evaluated using cosine similarity, so it aligns better with how the embeddings were trained.

# Why is HNSW approximate?

hnsw - hirarchical neighbouring samll world

HNSW builds a graph of similar vectors and searches it using a greedy traversal. It starts from a high-level layer, moves toward neighbors that appear increasingly closer to the query, and gradually descends to denser layers. Because it explores only promising paths instead of comparing the query with every vector or exhaustively searching the graph, it achieves very fast search times but cannot guarantee finding the mathematically exact nearest neighbor. In practice, with proper tuning, it typically achieves around 95–99% recall while reducing search latency by orders of magnitude. it gives  aclose enough aproximation context for the model to understand

The idea comes from social networks.
Imagine LinkedIn.
You don't know someone in Germany.
But you know someone.
Who knows someone.
Who knows them.

