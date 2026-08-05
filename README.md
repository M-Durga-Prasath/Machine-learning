# Machine Learning – Personal Learning Journey

This repository documents my personal, week-by-week journey of learning Machine Learning, Deep Learning, Computer Vision, NLP, and Production ML from the ground up. Every notebook, script, and note here is a record of what I studied, built, and experimented with.

> **This is a personal learning project.** The code and notes reflect my progress as I learn — they are not meant to be a polished library or production system.

---

## Curriculum Overview

| Week | Focus Area | Status |
|------|-----------|--------|
| [Week 1](#week-1--ml-foundations--pytorch) | ML Foundations & PyTorch | Complete |
| [Week 2](#week-2--deep-learning--cnns) | Deep Learning & CNNs | Complete |
| [Week 3](#week-3--computer-vision-with-yolo) | Computer Vision with YOLO | Complete |
| [Week 4](#week-4--transformers--production-ml) | Transformers & Production ML | Complete |
| [Week 5](#week-5--rag-foundations) | RAG Foundations | Complete |
| [Week 6](#week-6--hybrid-search--rag-evaluation) | Hybrid Search & RAG Evaluation | Complete |
| [Week 7](#week-7--finlens-flagship-project) | FinLens — Flagship Project | Complete |

---

## Capstone Projects

Each week culminates in a hands-on capstone project. Click through for detailed write-ups:

| Week | Project | Description |
|------|---------|-------------|
| Week 3 | [Autonomous Driving Perception Pipeline](week3/day7/) | YOLOv8 + ByteTrack multi-object tracking with danger-zone alerts, motion trails, and live analytics on dashcam video |
| Week 4 | [Dockerized Sentiment Analysis API](week4_transformers/day6/) | DistilBERT sentiment classifier served via FastAPI with a web UI, fully containerized with Docker Compose |
| Week 5 | [RAG Document Retrieval Pipeline](week5_ragfoundations/day4/) | PDF ingestion → chunking → sentence-transformer embeddings → FAISS vector search for semantic document retrieval |
| Week 7 | [FinLens — Finance RAG](https://github.com/M-Durga-Prasath/FinLens) | Flagship multi-file finance RAG application that answers user queries grounded in uploaded financial documents |

---

## Week 1 — ML Foundations & PyTorch

> Refer to [`week1/`](week1/) for all notebooks and notes.

Covered the fundamentals of machine learning and got hands-on with PyTorch (GPU-accelerated with CUDA).

| Day | Topic | File |
|-----|-------|------|
| Day 1 | Environment setup, PyTorch + CUDA installation | `setup-env.ipynb` |
| Day 2 | Linear Regression in PyTorch, PyTorch basics | `linear-reg.ipynb`, `pytorch.md` |
| Day 3 | Logistic Regression | `logistic-reg.ipynb` |
| Day 4 | Matrix operations & linear algebra | `matrix.ipynb` |
| Day 5 | End-to-end model building pipeline | `modelbuilding.ipynb` |
| Day 6 | Probability & simulation (coin flip experiments) | `coinflip.ipynb` |
| Day 7 | Car price prediction model, relationship testing | `carmodel.ipynb`, `relationtest.ipynb` |

---

## Week 2 — Deep Learning & CNNs

> Refer to [`week2/`](week2/) for all notebooks and notes.

Went deeper into neural networks, CNNs, transfer learning, and built a full image classifier.

| Day | Topic | File |
|-----|-------|------|
| Day 1 | PyTorch tensor basics & operations | `pytorchbasics.ipynb` |
| Day 2 | Building a neural network from scratch | `neuralnetwork.ipynb` |
| Day 3 | MNIST digit classification | `mnsit.ipynb` |
| Day 4 | Convolutional Neural Networks (CNNs) | `cnnmodel.ipynb` |
| Day 5 | Pretrained models & transfer learning (CIFAR) | `pretrained-model.ipynb` |
| Day 6 | Regularization techniques (dropout, weight decay) | `reqularization.ipynb` |
| Day 7 | **Capstone:** Vehicle classifier (trained & saved model) | `vehicleclassifier.ipynb` |

---

## Week 3 — Computer Vision with YOLO

> Refer to [`week3/`](week3/) for all notebooks and notes.

Explored real-time object detection, tracking, and built an autonomous driving perception mini-system.

| Day | Topic | File |
|-----|-------|------|
| Day 1 | YOLOv8 basics — first detection on images | `yolo.ipynb` |
| Day 2 | YOLOv8 on video — real-time detection | `yolov8prac.ipynb` |
| Day 3 | Data labelling & custom dataset preparation | `ddata.py` |
| Day 4 | Fine-tuning YOLOv8 on a custom vehicle dataset | `finetuning.ipynb` |
| Day 5 | Model evaluation metrics (mAP, precision, recall) | `modeleval.ipynb` |
| Day 6 | Multi-object tracking with ByteTrack | `tracking.ipynb` |
| Day 7 | **Capstone:** [Autonomous driving perception pipeline](week3/day7/) | `capstoneproj.ipynb` |

**Week 3 Capstone highlights:**
- YOLOv8 object detection + ByteTrack tracking
- Persistent track IDs, motion trails, FPS overlay
- Vehicle counting & pedestrian danger-zone alerts
- Full annotated output video saved to `output/`

---

## Week 4 — Transformers & Production ML

> Refer to [`week4_transformers/`](week4_transformers/) for all notebooks and notes.

Dove into the Transformer architecture, NLP model families, and production deployment patterns.

| Day | Topic | File |
|-----|-------|------|
| Day 1 | Transformer architecture — self-attention, Q/K/V | `transformers.ipynb` |
| Day 2 | Multi-head attention, positional encoding, tokenization | `transformers.ipynb` |
| Day 3 | Fine-tuning Transformers with Hugging Face Trainer API | `3ftransformers.ipynb` |
| Day 4 | Python production habits — decorators, logging, Docker intro | `decorator.py`, `docker.md` |
| Day 5 | Serving ML models with FastAPI + simple web UI | `app.py`, `index..html`, `model.ipynb` |
| Day 6 | **Capstone:** [Dockerized sentiment analysis API](week4_transformers/day6/) | `Dockerfile`, `compose.yaml`, `app.py` |

**Key topics covered:**
- Why Transformers replaced RNNs
- Scaled dot-product attention & multi-head attention
- BERT vs GPT vs T5 — when to use which
- Hugging Face ecosystem (models, tokenizers, datasets, Trainer)
- FastAPI + Pydantic for ML serving
- Docker containerization for reproducible ML deployments

---

## Week 5 — RAG Foundations

> Refer to [`week5_ragfoundations/`](week5_ragfoundations/) for all notebooks and notes.

Building the foundation for Retrieval-Augmented Generation (RAG) systems.

| Day | Topic | File |
|-----|-------|------|
| Day 1 | Text embeddings — sentence transformers, CLS vs mean pooling | `embeddings.ipynb` |
| Day 2 | Vector search theory — cosine similarity, HNSW, pgvector | `closeness.md` |
| Day 3 | Text chunking strategies for RAG | `chunking.ipynb` |
| Day 4 | **Capstone:** [RAG document retrieval pipeline](week5_ragfoundations/day4/) | `embed.py`, `retrival.py`, `simplerRAG.ipynb` |
| Day 5 | ML evaluation metrics — confusion matrix, precision, recall, F1, ROC-AUC | `notes.md` |
| Day 6 | Full RAG pipeline revision — tokenization, embeddings, retrieval deep-dive | `revise.md` |

**Key topics covered:**
- Why mean pooling > CLS pooling for semantic search
- Cosine similarity vs Euclidean distance
- HNSW (Hierarchical Navigable Small World) graphs
- pgvector — vector search inside PostgreSQL
- SQL window functions for RAG result ranking
- Chunking strategies for document processing
- FAISS for fast vector similarity search
- End-to-end RAG retrieval: PDF → chunk → embed → index → query
- ML evaluation: confusion matrix, precision, recall, F1, ROC-AUC

---

## Week 6 — Hybrid Search & RAG Evaluation

> Refer to [`week6_hybridsearch/`](week6_hybridsearch/) for all notebooks and notes.

Advanced retrieval techniques — combining sparse and dense search, re-ranking, RAG evaluation, and streaming LLM responses.

| Day | Topic | File |
|-----|-------|------|
| Day 1 | BM25 sparse retrieval, hybrid search & Reciprocal Rank Fusion (RRF) | `bm25.py`, `notes.md` |
| Day 2 | Domain shift in dense retrieval, BEIR benchmarking, RRF deep-dive | `hybrid.ipynb`, `notes.md` |
| Day 3 | Two-stage retrieval — Bi-Encoder vs Cross-Encoder re-ranking | `hybrid.ipynb`, `notes.md` |
| Day 4 | RAG evaluation — ground-truth datasets, retrieval & generation metrics | `evalrag.ipynb`, `create_gold_chunks.py` |
| Day 5 | Streaming LLM responses with FastAPI `StreamingResponse`, Pydantic models | `main.py`, `models.py`, `notes.md` |

**Key topics covered:**
- BM25 scoring & sparse vs dense retrieval trade-offs
- Reciprocal Rank Fusion for merging ranked lists
- Cross-Encoder re-ranking for precision over Bi-Encoder recall
- Building evaluation datasets with ground-truth Q&A pairs
- RAG retrieval metrics (hit rate, MRR) & generation metrics (faithfulness, relevance)
- FastAPI `StreamingResponse` for token-by-token LLM output

---

## Week 7 — FinLens (Flagship Project)

> **Flagship project repository:** [**FinLens**](https://github.com/M-Durga-Prasath/FinLens)

FinLens is the culminating flagship project of this learning journey — a full-stack Finance RAG application. It accepts multiple financial documents (PDFs, reports), ingests and indexes them, and answers user queries grounded in the uploaded content. This project brings together everything learned across the previous weeks — embeddings, vector search, hybrid retrieval, re-ranking, and LLM-powered generation — into a single, end-to-end production-style application.

---

## Tech Stack

- **Language:** Python
- **ML/DL:** PyTorch (CUDA), scikit-learn
- **Computer Vision:** Ultralytics YOLOv8, OpenCV
- **NLP:** Hugging Face Transformers, Sentence Transformers
- **RAG:** FAISS, LangChain, pypdf
- **Serving:** FastAPI, Pydantic
- **Deployment:** Docker, Docker Compose
- **Database:** PostgreSQL + pgvector
- **Data:** Pandas, NumPy, Matplotlib

---

## Project Structure

```
Machine-learning/
├── week1/                    # ML Foundations & PyTorch
│   ├── day1/ ... day7/
├── week2/                    # Deep Learning & CNNs
│   ├── day1/ ... day7/
├── week3/                    # Computer Vision (YOLO)
│   ├── day1/ ... day6/
│   └── day7/                 # Capstone: Perception Pipeline
├── week4_transformers/       # Transformers & Production ML
│   ├── day1/ ... day5/
│   ├── day6/                 # Capstone: Dockerized ML API
│   └── revision.md
├── week5_ragfoundations/     # RAG Foundations
│   ├── day1/ ... day3/
│   ├── day4/                 # Capstone: RAG Retrieval Pipeline
│   ├── day5/ ... day6/
│   └── revision.md
├── week6_hybridsearch/       # Hybrid Search & RAG Evaluation
│   ├── day1/ ... day5/
├── week7_finlens/            # Flagship Project: FinLens (separate repo)
├── data/                     # Datasets (CSV, Parquet, etc.)
├── testing/                  # Misc experiments & scripts
├── requirements.txt
└── README.md
```

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/M-Durga-Prasath/Machine-learning.git
cd Machine-learning

# Create a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows

# Install dependencies
pip install -r requirements.txt

# For PyTorch with CUDA (see week1/day2/pytorch.md for full guide)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
```

---
