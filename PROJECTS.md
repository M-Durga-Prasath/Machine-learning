# 🏆 Capstone Projects

This repo includes three hands-on capstone projects built at the end of Weeks 3, 4, and 5. Each one applies everything learned that week into a single, working system.

---

##  Autonomous Driving Perception Pipeline

**Week 3 · Day 7** — [`week3/day7/`](week3/day7/)

A mini self-driving perception system that processes dashcam video using **YOLOv8** for object detection and **ByteTrack** for multi-object tracking. The pipeline draws persistent track IDs, motion trails, and a live vehicle count on every frame. It also monitors a danger zone at the bottom of the frame and triggers an alert when a pedestrian enters it. The final annotated video is saved to `output/`.

**Stack:** YOLOv8 · ByteTrack · OpenCV · PyTorch

---

##  Dockerized Sentiment Analysis API

**Week 4 · Day 6** — [`week4_transformers/day6/`](week4_transformers/day6/)

A production-style ML API that serves a **DistilBERT** sentiment classifier through **FastAPI**. Send any sentence to the `/predict` endpoint and get back a `POSITIVE` / `NEGATIVE` label with a confidence score. Comes with a simple web UI for testing and is fully **Dockerized** — one `docker compose up --build` and the whole stack is running on port 8000.

**Stack:** FastAPI · Hugging Face Transformers · Docker · Docker Compose

---

##  RAG Document Retrieval Pipeline

**Week 5 · Day 4** — [`week5_ragfoundations/day4/`](week5_ragfoundations/day4/)

The retrieval half of a **Retrieval-Augmented Generation (RAG)** system. It reads PDF documents, chunks the text with LangChain's `RecursiveCharacterTextSplitter`, generates 384-dim embeddings using **Sentence Transformers** (`all-MiniLM-L6-v2`), and indexes them in a **FAISS** vector store. At query time, your natural-language question is embedded and matched against the index to return the top-5 most relevant passages with source metadata.

**Stack:** Sentence Transformers · FAISS · LangChain · pypdf

---

> Each project folder has its own detailed `README.md` with architecture diagrams, file descriptions, setup instructions, and what I learned.
