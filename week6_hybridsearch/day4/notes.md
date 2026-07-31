
## Key Terms

### Evaluation Dataset
A collection of predefined questions along with their correct answers and/or correct document chunks. It is used to consistently evaluate and compare the performance of a RAG system.

---

### Ground Truth
The verified, correct answer for a question. It serves as the reference answer during evaluation.

**Example**

**Question:** What embedding model does this project use?

**Ground Truth:** all-MiniLM-L6-v2

---

### Gold Answer
The ideal answer that the RAG system should generate. In most cases, it is the same as the Ground Truth answer but written as a complete response.

**Example**

**Question:** What is BM25?

**Gold Answer:** BM25 is a keyword-based retrieval algorithm that ranks documents using term frequency and inverse document frequency.

---

### Gold Chunk
The document chunk that contains the information needed to answer a question correctly.

**Example**

If Chunk #42 explains BM25, then Chunk #42 is the **Gold Chunk** for the question:

> What is BM25?

---

### Retrieval Hit Rate
A retrieval metric that measures how often the retriever successfully finds the Gold Chunk.

**Formula**

```text
Hit Rate = (Number of Successful Retrievals / Total Questions) × 100
```

**Example**

```text
Correct Retrievals = 8
Total Questions = 10

Hit Rate = (8 / 10) × 100 = 80%
```

---

### Hallucination
When the LLM generates information that is not supported by the retrieved documents or invents facts instead of admitting it doesn't know.

**Example**

**Question:** Which database does this project use?

**Documents:** No database is mentioned.

**LLM Answer:** It uses PostgreSQL.

This is a **Hallucination** because the information is fabricated.

---

### LLM-as-a-Judge
Using another LLM to automatically evaluate generated answers by comparing them against the Ground Truth.

Instead of a human checking every answer, an LLM scores correctness, relevance, faithfulness, or completeness.

---

### Benchmark Dataset
A fixed evaluation dataset that is reused whenever the RAG system changes, allowing fair comparison between different versions.

---

### Evaluation Harness
An automated pipeline that evaluates the RAG system by running benchmark questions, comparing outputs with Ground Truth, and calculating evaluation metrics.

**Workflow**

```text
Question
      ↓
Retriever
      ↓
Retrieved Chunks
      ↓
LLM
      ↓
Generated Answer
      ↓
Compare with Ground Truth
      ↓
Compute Metrics
      ↓
Final Evaluation Score
```

---

## Difficulty Levels

### Level 1 — Single-Fact Lookup

The answer exists entirely within one document chunk.

**Example**

**Question:** What embedding model does this project use?

Only one chunk contains the answer.

---

### Level 2 — Multi-Chunk Synthesis

The answer requires combining information from multiple retrieved chunks.

**Example**

Chunk A:

> Hybrid retrieval combines Dense Retrieval and BM25.

Chunk B:

> Reciprocal Rank Fusion (RRF) merges rankings from both retrievers.

**Question**

How does hybrid retrieval improve RAG performance?

The LLM must combine information from both chunks.

---

### Level 3 — Not in Corpus

The answer does not exist anywhere in the provided documents.

A good RAG system should answer:

> I don't know.

instead of making something up.

**Example**

**Question:** Who invented the Transformer architecture?

If the documents do not mention it, the correct response is:

> The information is not available in the provided documents.

---

## Why RAG Evaluation is Difficult

A good-looking answer does not necessarily mean the RAG system worked correctly.

The LLM might:
- Already know the answer from pretraining.
- Retrieve the wrong documents.
- Ignore the retrieved context.
- Hallucinate information.

Therefore, both retrieval quality and generation quality must be evaluated separately.

---

## 1. What is a Ground Truth answer?

A **Ground Truth** answer is the verified and correct answer for a question. It acts as the reference answer against which the RAG system's generated answer is compared during evaluation.

---

## 2. Why do evaluation datasets contain different difficulty levels?

Evaluation datasets contain different difficulty levels to test multiple capabilities of a RAG system.

- **Single-Fact Lookup** tests whether the retriever can locate simple information.
- **Multi-Chunk Synthesis** tests whether the model can combine information from multiple retrieved chunks.
- **Not in Corpus** tests whether the model avoids hallucinating when the answer is unavailable.

Using different difficulty levels provides a more realistic evaluation of the system.

---

## 3. Why are "Not in Corpus" questions important?

"Not in Corpus" questions measure **hallucination resistance**.

If the required information does not exist in the documents, a good RAG system should respond with **"I don't know"** or indicate that the information is unavailable instead of inventing an answer.

---

## 4. Why is retrieval evaluation separate from generation evaluation?

Retrieval evaluation and generation evaluation measure different components of a RAG pipeline.

- **Retrieval Evaluation** checks whether the retriever finds the correct **Gold Chunk** (e.g., using **Retrieval Hit Rate**).
- **Generation Evaluation** checks whether the LLM generates a correct answer using the retrieved context.

Separating these evaluations helps identify whether errors originate from retrieval or answer generation.

---

## Quick Revision Table


| Term | Meaning |
|------|---------|
| Evaluation Dataset | Set of benchmark questions and answers used for evaluation |
| Ground Truth | Verified correct answer |
| Gold Answer | Ideal response the LLM should generate |
| Gold Chunk | Correct document chunk containing the answer |
| Retrieval Hit Rate | Percentage of questions where the correct chunk was retrieved |
| Hallucination | LLM invents unsupported information |
| LLM-as-a-Judge | LLM automatically evaluates generated answers |
| Benchmark Dataset | Fixed evaluation dataset used across experiments |
| Evaluation Harness | Automated pipeline for evaluating a RAG system |
| Single-Fact Lookup | Answer found in one chunk |
| Multi-Chunk Synthesis | Answer requires multiple chunks |
| Not in Corpus | Answer does not exist in the documents; model should say "I don't know." |



## 1. How do you evaluate a RAG system?

A RAG (Retrieval-Augmented Generation) system is evaluated by measuring both **retrieval performance** and **generation performance**.

- **Retrieval Evaluation:** Determines whether the retriever fetched the correct and relevant chunks from the knowledge base.
- **Generation Evaluation:** Determines whether the LLM generated a correct, complete, and faithful answer using the retrieved context.

Evaluating these separately helps identify whether failures originate from retrieval or answer generation.

---

## 2. What is Hit Rate@K?

**Hit Rate@K** is a retrieval metric that measures how often at least one relevant (gold) chunk appears within the top **K** retrieved results.

### Formula

```text
Hit Rate@K =
(Number of questions with at least one gold chunk in Top-K)
/
(Total number of questions)
```

### Example

- Total Questions = 20
- Gold chunk found in Top-5 for 18 questions

```text
Hit Rate@5 = 18 / 20 = 90%
```

A higher Hit Rate indicates a better retrieval system.

---

## 3. Why separate retrieval errors from generation errors?

Retrieval and generation solve different problems.

- If the retriever fails to fetch the correct information, the LLM has insufficient context and may hallucinate or answer incorrectly.
- If the retriever provides the correct context but the LLM still produces an incorrect answer, the issue lies in the generation model.

Separating these evaluations helps identify the root cause of failures and makes debugging more effective.

---

## 4. What makes a good evaluation dataset?

A good evaluation dataset should:

- Cover easy, medium, and difficult questions.
- Include questions requiring information from multiple chunks.
- Contain clear and accurate gold answers.
- Include the corresponding gold chunk IDs for retrieval evaluation.
- Include "answer not in corpus" questions to test hallucination handling.
- Be representative of real user queries.

A balanced dataset provides a more reliable assessment of both retrieval and generation performance.

---

# Production

## 5. What is an evaluation harness?

An **evaluation harness** is an automated pipeline that measures the performance of a RAG system.

It typically:

1. Loads an evaluation dataset.
2. Runs each question through the retrieval pipeline.
3. Generates an answer using the RAG system.
4. Compares retrieved chunks with the gold chunks.
5. Evaluates generated answers against the gold answers.
6. Computes evaluation metrics such as Hit Rate@K and Generation Accuracy.
7. Saves the evaluation results for analysis.

An evaluation harness ensures consistent and repeatable evaluation whenever the RAG system is updated.

---

## 6. Why use an LLM-as-a-Judge?

An **LLM-as-a-Judge** evaluates generated answers by comparing them with reference (gold) answers.

It is useful because:

- Exact string matching is too strict.
- Correct answers can be phrased differently.
- The judge can evaluate semantic similarity rather than exact wording.
- It can classify responses as:
  - Correct
  - Partially Correct
  - Incorrect

Using an LLM judge provides a more realistic evaluation of answer quality.

---

## 7. Why include "answer not in corpus" questions?

These questions test whether the RAG system correctly identifies when information is unavailable.

A good RAG system should respond with something like:

> "The information is not available in the provided documents."

instead of hallucinating or inventing an answer.

Including these questions measures the system's ability to avoid generating unsupported information.

---

## 8. How do you demonstrate that a retrieval improvement actually works?

A retrieval improvement should be demonstrated using quantitative evaluation metrics rather than subjective examples.

For example, compare multiple retrieval pipelines using the same evaluation dataset:

| Pipeline | Hit Rate@5 |
|----------|-----------:|
| Dense Retrieval | 72% |
| BM25 | 68% |
| Hybrid Retrieval | 84% |
| Hybrid + RRF | 91% |
| Hybrid + Reranker | 95% |

If the improved retriever consistently achieves a higher Hit Rate@5 (or other retrieval metrics), it provides objective evidence that the retrieval pipeline has improved.