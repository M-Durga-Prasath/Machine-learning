# Week 1 Revision Notes – Transformer Foundations + Production Habits

---

# 1. Why Transformers?

## Q: Why were Transformers invented?

**Answer**

- RNNs process tokens sequentially, making training slow.
- They struggle with long-range dependencies due to vanishing gradients.
- Transformers replace recurrence with **Self-Attention**, allowing every token to attend to every other token directly.
- This enables parallel computation and significantly faster training.

---

## Q: Why are Transformers faster than RNNs?

**Answer**

RNNs process one token after another because each hidden state depends on the previous one.

Transformers process the entire sequence simultaneously using matrix operations, which GPUs are optimized for.

---

## Q: What problem does Self-Attention solve?

**Answer**

Self-Attention lets every token dynamically determine which other tokens are important for understanding its meaning, regardless of their position.

---

## Q: Example where attention helps?

**Answer**

Sentence:

> "The animal didn't cross the street because **it** was too tired."

The word **"it"** should attend strongly to **"animal"**, not **"street."**

---

# 2. Self-Attention

## Q: What are Query, Key and Value?

**Answer**

Every token is projected into three vectors.

- **Query (Q)** → What information this token is looking for.
- **Key (K)** → What information this token offers.
- **Value (V)** → The actual information passed forward.

Attention compares Queries with Keys to decide how much of each Value to use.

---

## Q: What does Softmax(QKᵀ / √dk) produce?

**Answer**

It produces the **attention weights**.

Each row is a probability distribution showing how much one token attends to every other token.

Rows always sum to **1**.

---

## Q: Why divide by √dk?

**Answer**

Without scaling, dot products become very large as vector dimensions increase.

Large values push Softmax into saturation, causing very small gradients.

Scaling keeps training stable.

---

## Q: Why Softmax?

**Answer**

Softmax converts similarity scores into probabilities.

These probabilities determine how much information should be gathered from each token.

---

## Q: Why Multi-Head Attention?

**Answer**

Different attention heads learn different relationships simultaneously.

For example:

- Grammar
- Subject-object relationships
- Long-range dependencies

Multiple heads create richer representations than a single attention calculation.

---

## Q: What is Causal Masking?

**Answer**

It prevents tokens from attending to future tokens.

Used in GPT because text generation must only depend on previously generated words.

---

# 3. Positional Encoding

## Q: Why do Transformers need Positional Encoding?

**Answer**

Transformers process tokens in parallel.

Without positional information they don't know the order of words.

Positional Encoding injects sequence information into token embeddings.

---

## Q: Why don't RNNs need Positional Encoding?

**Answer**

Because RNNs naturally process tokens sequentially.

Order is already encoded by computation.

---

# 4. Tokenization

## Q: Why don't we tokenize by whole words?

**Answer**

- Vocabulary becomes extremely large.
- New words appear constantly.
- Unknown words become impossible to represent.

Subword tokenization solves these problems.

---

## Q: What is BPE?

**Answer**

Byte Pair Encoding repeatedly merges frequently occurring character pairs into subwords.

---

## Q: WordPiece vs BPE?

**Answer**

Both generate subword vocabularies.

- **BPE** merges the most frequent pairs.
- **WordPiece** chooses merges that maximize language model likelihood.

---

# 5. Transformer Families

## Q: What is BERT?

**Answer**

- Encoder-only Transformer
- Trained using Masked Language Modeling
- Designed for understanding text

Applications:

- Sentiment Analysis
- NER
- Question Answering
- Text Classification

---

## Q: What is GPT?

**Answer**

- Decoder-only Transformer
- Trained using Next Token Prediction
- Designed for text generation

Applications:

- Chatbots
- Story generation
- Code generation

---

## Q: What is T5?

**Answer**

- Encoder-Decoder Transformer
- Everything is framed as Text → Text

Applications:

- Translation
- Summarization
- Grammar Correction
- Question Answering

---

## Q: Which model should be used for NER?

**Answer**

**BERT**

Because it understands both left and right context.

---

## Q: Which model should be used for Text Generation?

**Answer**

**GPT**

Because it predicts the next token autoregressively.

---

## Q: Which model should be used for Translation?

**Answer**

**T5**

Because Encoder-Decoder models first understand the input before generating transformed output.

---

# 6. Hugging Face

## Q: Why Hugging Face?

**Answer**

It provides:

- Pretrained Models
- Tokenizers
- Datasets
- Trainer API
- Pipelines

allowing rapid ML development.

---

## Q: What does Trainer API do?

**Answer**

It automates:

- Training
- Validation
- Evaluation
- Logging
- Checkpoint Saving

---

# 7. FastAPI

## Q: Why FastAPI over Flask?

**Answer**

FastAPI provides:

- Automatic Request Validation
- Async Support
- Automatic Swagger Documentation
- Better Performance
- Strong Type Hints via Pydantic

---

## Q: Why Pydantic?

**Answer**

Pydantic validates request data automatically.

It also generates API documentation.

---

## Q: Why load the model only once?

**Answer**

Loading a transformer model is expensive.

Load it once during application startup and reuse it for all requests.

---

## Q: Why async?

**Answer**

Async doesn't speed up CPU-bound inference.

It becomes valuable when waiting for:

- Databases
- APIs
- Vector Databases
- File Systems

---

# 8. Docker

## Q: What is a Docker Image?

**Answer**

A read-only blueprint containing everything required to run an application.

---

## Q: What is a Docker Container?

**Answer**

A running instance of an Image.

---

## Q: Why copy requirements.txt first?

**Answer**

Docker caches layers.

Since dependencies change less frequently than source code, copying requirements first avoids reinstalling packages during every rebuild.

---

## Q: Why python:3.11-slim?

**Answer**

Smaller image size while retaining everything needed to run the application.

---

## Q: Why Dockerize an ML API?

**Answer**

To package:

- Model
- Dependencies
- Runtime

into a reproducible environment that behaves identically across machines.

---

# 9. Python Production Habits

## Q: What is a Decorator?

**Answer**

A function that wraps another function to extend its behavior without modifying the original implementation.

---

## Q: What does @timer actually do?

**Answer**

Python transforms

```python
@timer
def predict():
```

into

```python
predict = timer(predict)
```

The decorator adds timing functionality while preserving the original function.

---

## Q: Why Logging instead of print()?

**Answer**

Logging provides:

- Timestamps
- Severity Levels
- Better Debugging
- File Logging
- Configurable Output

making it suitable for production systems.

---

# 10. Week 1 Project

## Q: Explain your project in 60 seconds.

**Answer**

I built a production-ready Sentiment Analysis API using DistilBERT, FastAPI, Docker, and Hugging Face.

The model loads once during application startup to minimize inference latency.

Users send text through a POST endpoint.

FastAPI validates the request using Pydantic.

DistilBERT performs inference.

The API returns the predicted sentiment and confidence score as JSON.

The application is documented using Swagger and containerized with Docker for reproducible deployment.


```

Make this personal rather than memorizing it.

---


- [ ] Why Transformers replaced RNNs
- [ ] Query, Key and Value
- [ ] Scaled Dot Product Attention
- [ ] Multi-Head Attention
- [ ] Positional Encoding
- [ ] BPE vs WordPiece
- [ ] BERT vs GPT vs T5
- [ ] Hugging Face ecosystem
- [ ] FastAPI + Pydantic
- [ ] Docker Images vs Containers
- [ ] Python Decorators & Logging
- [ ] Architecture of your Sentiment Analysis API

---


- Implement Scaled Dot Product Attention from scratch.
- Explain Multi-Head Attention intuitively.
- Differentiate BERT, GPT, and T5.
- Use Hugging Face models and Trainer API.
- Build and serve ML models using FastAPI.
- Containerize ML applications using Docker.
- Write production-quality Python using decorators and logging.
- Build, document, and deploy a production-style Sentiment Analysis API.