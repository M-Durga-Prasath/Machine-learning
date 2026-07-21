
## Vector Search, HNSW, pgvector & SQL Window Functions

# 1. Why doesn't brute-force vector search scale?

### Answer

Brute-force vector search compares the query embedding with **every embedding** stored in the database.

For example:

- 10 documents → 10 similarity calculations
- 1 million documents → 1 million similarity calculations
- 10 million documents → 10 million similarity calculations

If each embedding has 384 dimensions, millions of floating-point operations are required for every search.

The time complexity is **O(n)** because every vector must be checked.

As the number of users and documents increases, latency and computational cost grow linearly, making brute-force search impractical for production systems.

### Interview Tip

Mention that brute-force provides **100% recall** because every vector is compared, but this comes at the cost of high latency.

---

# 2. What is Approximate Nearest Neighbor (ANN)?

### Answer

Approximate Nearest Neighbor (ANN) is a search technique that finds vectors that are **very close** to the query rather than guaranteeing the mathematically closest vector.

Instead of searching every document, ANN intelligently searches only the most promising regions of the vector space.

Imagine searching for a restaurant in Mumbai.

Instead of visiting every restaurant, you first go to the correct neighborhood and then search nearby.

That's exactly how ANN works.

### Advantages

- Extremely fast
- Low latency
- Scales to millions of vectors
- Nearly identical retrieval quality

### Trade-off

- Doesn't always return the exact nearest vector.
- Usually returns a vector that's almost identical.

---

# 3. Why is ANN acceptable for RAG?

### Answer

Large Language Models do not require the mathematically closest document.

They only require **highly relevant context**.

Suppose the true nearest document has a cosine similarity of **0.98**.

ANN returns another document with similarity **0.97**.

The retrieved information is still almost identical.

The LLM will likely generate the same answer.

This is why production RAG systems prioritize **speed over perfect accuracy**.

---

# 4. Why don't KD Trees or Ball Trees work well for embeddings?

### Answer

KD Trees and Ball Trees are designed for low-dimensional data.

Examples:

- 2 dimensions
- 3 dimensions
- 10 dimensions

Modern embedding models produce vectors with:

- 384 dimensions
- 768 dimensions
- 1024 dimensions
- 1536 dimensions

As dimensionality increases, distances between points become less meaningful.

This phenomenon is called the **Curse of Dimensionality**.

As a result, traditional tree-based indexes lose efficiency and often become no faster than brute-force search.

---

# 5. What is HNSW?

### Answer

HNSW stands for

**Hierarchical Navigable Small World**

It is one of the most popular Approximate Nearest Neighbor algorithms.

It organizes vectors into multiple graph layers.

```
Layer 3

      A ----- B

Layer 2

A --- C --- D --- E

Layer 1

Thousands of connected nodes
```

### Search Process

1. Start at the top layer.
2. Move toward nodes closer to the query.
3. Descend layer by layer.
4. Perform a detailed search in the bottom layer.

Because only a small portion of the graph is explored, HNSW is extremely fast.

---

# 6. Why is HNSW approximate?

### Answer

HNSW performs **greedy graph traversal**.

Instead of checking every vector, it keeps moving toward neighbors that appear closer to the query.

Since it doesn't explore every possible path, it may miss the mathematically closest vector.

However, it almost always finds a very similar one.

### Interview Answer

> HNSW performs a greedy graph traversal rather than exhaustively comparing every embedding. It searches only promising regions of the graph, which makes it extremely fast but approximate.

---

# 7. What is pgvector?

### Answer

pgvector is a PostgreSQL extension that adds support for storing and searching vector embeddings.

After installation,

```sql
CREATE EXTENSION vector;
```

PostgreSQL gains a new datatype.

```sql
CREATE TABLE documents(
    id SERIAL PRIMARY KEY,
    text TEXT,
    embedding VECTOR(384)
);
```

Now PostgreSQL stores both

- relational data
- vector embeddings

inside the same database.

---

# 8. Why use pgvector instead of Pinecone?

### Answer

pgvector is ideal when:

- Your metadata already lives in PostgreSQL.
- Your embeddings are moderate in size.
- You want a simpler architecture.
- You want lower infrastructure costs.

Dedicated vector databases like Pinecone become useful when:

- You have hundreds of millions of vectors.
- You require distributed indexing.
- You need specialized vector search features.

### Interview Answer

> pgvector keeps relational data and embeddings together, reducing operational complexity and cost. Dedicated vector databases become useful at much larger scales.

---

# 9. How do you perform similarity search in pgvector?

### Answer

```sql
SELECT *
FROM documents
ORDER BY embedding <=> query_embedding
LIMIT 5;
```

The operator

```
<=>
```

computes cosine distance.

Smaller distance means

Higher similarity.

Without an index, PostgreSQL compares every row.

---

# 10. Why create an HNSW index?

### Answer

Without an index

```
Query

↓

Compare row 1

↓

Compare row 2

↓

Compare row 3

↓

...

↓

Compare every row
```

Time complexity remains O(n).

Creating an HNSW index

```sql
CREATE INDEX
ON documents
USING hnsw (embedding vector_cosine_ops);
```

allows PostgreSQL to navigate a graph instead of scanning every embedding.

Result:

- Faster retrieval
- Lower latency
- Better scalability

---

# 11. What does the `m` parameter control?

### Answer

`m` controls how many neighbors each node stores inside the HNSW graph.

Higher `m`

- Better recall
- More graph connections
- Larger index
- More memory usage
- Slower index creation

Lower `m`

- Smaller graph
- Faster builds
- Less memory
- Slightly lower recall

Think of `m` as the number of friends every node keeps.

---

# 12. What are `ef_construction` and `ef_search`?

## ef_construction

Controls how thoroughly PostgreSQL builds the graph.

Higher values mean

- Better graph quality
- Better recall
- Longer index build time

---

## ef_search

Controls how many candidate nodes PostgreSQL explores while searching.

Higher values mean

- Better accuracy
- Better recall
- Higher search latency

### Easy Way to Remember

- **ef_construction** → Build time parameter.
- **ef_search** → Query time parameter.

---

# 13. Why is cosine similarity commonly used?

### Answer

Embedding models encode semantic meaning in the **direction** of vectors.

Cosine similarity measures the angle between vectors rather than their magnitude.

This makes it ideal for semantic search.

Two vectors pointing in nearly the same direction represent similar meanings even if their lengths differ.

---

# 14. What are SQL Window Functions?

### Answer

A window function performs calculations across related rows **without collapsing them**.

Unlike

```sql
GROUP BY
```

which returns one row per group,

Window Functions keep every row while adding computed values.

Examples include

- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- SUM()
- AVG()
- LAG()
- LEAD()

Example

```sql
SELECT
    session_id,
    score,
    RANK() OVER(
        PARTITION BY session_id
        ORDER BY score DESC
    ) AS rank
FROM retrieval_results;
```

---

# 15. Why use `RANK() OVER(PARTITION BY ... ORDER BY ...)` in RAG?

### Answer

Suppose retrieval returns

```
Session 1

Doc A 0.95

Doc B 0.91

Doc C 0.82

Session 2

Doc X 0.98

Doc Y 0.90
```

Using

```sql
RANK() OVER(
PARTITION BY session_id
ORDER BY score DESC
)
```

produces

```
Session 1

Doc A Rank 1

Doc B Rank 2

Doc C Rank 3

Session 2

Doc X Rank 1

Doc Y Rank 2
```

Each session gets its own ranking.

This makes selecting the **Top-K** documents for every query straightforward.

---


