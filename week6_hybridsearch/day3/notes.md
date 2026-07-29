# Two-Stage Retrieval & Re-ranking \

---

# 1. Bi-Encoder

## Definition

A **Bi-Encoder** encodes the **query** and **document independently** into embeddings (vectors).

```
Query --------> Embedding

Document -----> Embedding
```

The embeddings are then compared using vector similarity (Cosine Similarity, Dot Product, etc.).

---

## Key Points

- Query encoded independently
- Document encoded independently
- Produces embeddings
- Embeddings can be precomputed
- Very fast retrieval
- Lower ranking accuracy
- Used for Initial Retrieval / Candidate Generation

---

## Advantages

- Extremely fast
- Scales to millions of documents
- Embeddings stored in Vector DB
- Low retrieval latency

---

## Disadvantages

- Query and document never interact while encoding
- Misses fine-grained context
- Lower ranking quality

---

# 2. Cross-Encoder

## Definition

A **Cross-Encoder** processes the **query and document together** using cross-attention.

```
(Query + Document)

↓

Cross-Encoder

↓

Relevance Score
```

It **does not create embeddings**.

It directly predicts:

> "How relevant is this document for this query?"

---

## Key Points

- Query and document processed together
- Uses Cross-Attention
- Produces a relevance score
- No reusable embeddings
- Cannot be pre-indexed
- Much slower
- Higher ranking accuracy
- Used for Re-ranking

---

## Advantages

- Best ranking quality
- Understands context better
- High precision
- Excellent Query-Document Pair Scoring

---

## Disadvantages

- Slow
- Expensive
- Cannot precompute results
- Not suitable for searching millions of documents

---

# 3. Candidate Generation

## Definition

Candidate Generation is the first retrieval stage where the system retrieves a larger set of potentially relevant documents.

Example:

```
100,000 Documents

↓

Bi-Encoder

↓

Top 20 Candidates
```

The goal is **high Recall**, not perfect ranking.

---

# 4. Re-ranking

## Definition

Re-ranking means taking the candidate documents and ranking them more accurately using a Cross-Encoder.

```
Top 20

↓

Cross-Encoder

↓

Top 5
```

Goal:

Increase Precision.

---

# 5. Two-Stage Retrieval

## Definition

A retrieval pipeline consisting of:

```
User Query

↓

Bi-Encoder

↓

Top 20 Candidates

↓

Cross-Encoder

↓

Top 5 Results
```

Stage 1 focuses on speed.

Stage 2 focuses on accuracy.

---

# 6. Cross-Attention

Instead of encoding separately:

```
Query

Document
```

Cross-Attention lets every query word attend to every document word.

Example:

```
Query:
Reset VPN Password

↓

Document:
Employees can change VPN credentials.
```

The model learns:

- reset ≈ change
- password ≈ credentials

This improves ranking quality.

---

# 7. Query-Document Pair Scoring

Cross-Encoder evaluates:

```
(Query, Document)

↓

Score = 9.8
```

Higher score = More Relevant

Every query-document pair gets a new score.

---

# 8. Retrieval Latency

Retrieval Latency = Time taken to retrieve documents.

Bi-Encoder

- Low latency
- Fast

Cross-Encoder

- High latency
- Slow

Production systems try to keep latency low while maintaining high accuracy.

---

# 9. Precision vs Recall

## Recall

> Did we retrieve all potentially relevant documents?

High Recall means fewer good documents are missed.

Candidate Generation aims for high Recall.

---

## Precision

> Are the returned documents actually relevant?

High Precision means fewer irrelevant documents appear.

Re-ranking aims for high Precision.

---

# 10. Why Cross-Encoder Cannot Be Pre-indexed

Cross-Encoder computes:

```
(Query + Document)

↓

Score
```

Since the score depends on both the query and document, a new query produces a different score.

Example:

```
Reset VPN

↓

Doc A = 9.6
```

```
Connect VPN

↓

Doc A = 6.8
```

Because future queries are unknown, scores cannot be computed beforehand.

Hence:

❌ Cannot be pre-indexed.

---

# 11. Why Bi-Encoder Can Be Precomputed

Bi-Encoder creates:

```
Document

↓

Embedding
```

This embedding represents the document's semantic meaning and does not depend on any specific query.

When a new query arrives:

```
Query

↓

Embedding

↓

Compare against stored document embeddings
```

Only the query embedding changes.

The document embeddings remain reusable.

Hence:

✅ Can be pre-indexed.

---

# 12. Why Top-20 → Top-5?

Suppose fast retrieval ranks:

```
1
2
3
4
5
6
7 ← Actually Best
```

If you retrieve only Top-5,

Document 7 is lost forever.

Instead:

```
Retrieve Top-20

↓

Cross-Encoder Re-ranks

↓

7
2
1
5
3
```

This improves final ranking quality.

---

# Production Pipeline

```
User Query

↓

Bi-Encoder

↓

Candidate Generation (Top 20)

↓

Cross-Encoder

↓

Re-ranking

↓

Top 5

↓

LLM
```

---

# Common Interview Questions

## Q1. Why not use a Cross-Encoder on every document?

**Answer:**

Because a Cross-Encoder processes every query-document pair separately using cross-attention. For millions of documents, this would require millions of model inferences, making retrieval latency too high for production systems.

---

## Q2. Why retrieve Top-20 and then re-rank to Top-5 instead of directly retrieving Top-5?

**Answer:**

The Bi-Encoder is fast but not perfectly accurate. The truly best document may initially rank outside the Top-5 (e.g., 7th or 15th). Retrieving a larger candidate set increases Recall, allowing the Cross-Encoder to accurately re-rank and improve Precision.

---

## Q3. Why can Bi-Encoder embeddings be precomputed but Cross-Encoder scores cannot?

**Answer:**

A Bi-Encoder creates independent document embeddings that are reusable for any query. A Cross-Encoder doesn't create reusable embeddings—it computes a relevance score for each specific query-document pair. Since future queries are unknown, these scores cannot be precomputed.

---

## Q4. What is the difference between a Bi-Encoder and a Cross-Encoder?

**Answer:**

A Bi-Encoder encodes the query and document independently into embeddings and compares them using vector similarity. A Cross-Encoder processes the query and document together using cross-attention and directly predicts a relevance score. Bi-Encoders are faster, while Cross-Encoders are more accurate.

---

## Q5. Why do production RAG systems use Two-Stage Retrieval?

**Answer:**

Production RAG systems need both speed and accuracy. A Bi-Encoder quickly retrieves a high-recall candidate set, and a Cross-Encoder re-ranks those candidates with higher precision. This balances retrieval latency, computational cost, and ranking quality.



# Retry with Exponential Backoff

## Why Retry Logic?

LLM APIs can fail temporarily due to:

- Rate limits
- Network issues
- Server errors
- Timeouts

Instead of failing immediately, retrying improves application reliability.

---

## Exponential Backoff

Retry delays increase exponentially.

Example:

Retry 1 → 1 sec

Retry 2 → 2 sec

Retry 3 → 4 sec

If all retries fail, raise the exception.

Advantages:

- Reduces server load
- Handles transient failures
- Improves production reliability

---

## Retry Decorator

A retry decorator wraps a function and automatically retries failed API calls without duplicating retry logic.

Example:

```python
@retry_with_backoff
def call_llm():
    ...
```

---

# Python Generators

A generator is a function that uses `yield` instead of `return`.

Example:

```python
def stream(tokens):
    for token in tokens:
        yield token
```

Generators produce values one at a time instead of all at once.

---

# Lazy Evaluation

Lazy evaluation computes values only when they are requested.

Benefits:

- Lower memory usage
- Better performance for large outputs
- Enables streaming

---

# Streaming Responses

Instead of waiting for the complete LLM response, tokens are sent as they are generated.

Benefits:

- Lower perceived latency
- Better user experience
- Compatible with FastAPI's `StreamingResponse`

---

# return vs yield

| return                                            | yield                                      |
|---------------------------------------------------|--------------------------------------------|
| Ends the function                                 | Pauses the function                        |
| Returns all data at once                          | Produces one value at a time               |        
| Cannot resume                                     | Resumes execution                          |
| Eager evaluation                                  | Lazy evaluation                            |

---