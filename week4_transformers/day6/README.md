# 🐳 Week 4 Capstone — Dockerized Sentiment Analysis API

> **Location:** `week4_transformers/day6/`
> **Main entry point:** [`app.py`](app.py)

---

## What This Project Does

This project wraps a **Hugging Face sentiment analysis model** inside a **FastAPI web server** and packages the whole thing into a **Docker container** for reproducible deployment. It's a full end-to-end example of taking an ML model from notebook to production-ready API.

### Architecture

```
User (Browser / cURL)
        │
        ▼
  ┌────────────┐
  │  Frontend   │   ← index..html (simple  web UI)
  │  (Browser)  │
  └─────┬──────┘
        │ POST /predict
        ▼
  ┌────────────┐
  │  FastAPI    │   ← app.py (REST API with CORS)
  │  Server     │
  └─────┬──────┘
        │
        ▼
  ┌────────────┐
  │ DistilBERT │   ← model_loader.py (HF pipeline)
  │  Model     │
  └────────────┘
```

### How It Works

1. The **model** (`distilbert-base-uncased-finetuned-sst-2-english`) is loaded once at startup via a Hugging Face `text-classification` pipeline
2. The **FastAPI server** exposes a `POST /predict` endpoint that accepts a JSON body `{"text": "your sentence"}`
3. The model classifies the text as `POSITIVE` or `NEGATIVE` with a confidence score
4. A simple **dark-mode HTML frontend** lets you type sentences and see results in real time
5. The whole stack is **Dockerized** — one `docker compose up --build` and it's running

---

## Files

| File | Description |
|------|-------------|
| `app.py` | FastAPI application with `/predict` and `/test` endpoints |
| `model_loader.py` | Loads the DistilBERT sentiment classifier at import time |
| `index..html` | Dark-mode web UI for testing predictions |
| `Dockerfile` | Multi-stage Docker build for the Python app |
| `compose.yaml` | Docker Compose config — maps port 8000 |
| `model.ipynb` | Notebook for experimenting with the model |
| `requirements.txt` | Python dependencies (FastAPI, Transformers, PyTorch) |
| `.dockerignore` | Files excluded from the Docker build context |
| `README.Docker.md` | Docker-generated deployment guide |

---

## Tech Stack

- **Model:** DistilBERT (Hugging Face Transformers)
- **API Framework:** FastAPI + Pydantic
- **Server:** Uvicorn
- **Frontend:** Vanilla HTML/CSS/JS
- **Containerization:** Docker + Docker Compose

---

## How to Run

### Option 1 — Docker (recommended)

```bash
# Build and start the container
docker compose up --build

# API is now live at http://localhost:8000
```

### Option 2 — Local

```bash
# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app:app --reload

# Open index..html in your browser (via Live Server or similar)
```

### Test the API

```bash
# Health check
curl http://localhost:8000/test

# Predict sentiment
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This movie was absolutely fantastic!"}'
```

**Example response:**
```json
{
  "text": "This movie was absolutely fantastic!",
  "label": "POSITIVE",
  "score": 0.9998,
  "message": "POSITIVE (1.000)"
}
```

---

## What I Learned

- How to serve ML models with FastAPI + Pydantic request validation
- Loading Hugging Face pipelines as a shared module to avoid re-loading on every request
- CORS middleware configuration for frontend ↔ API communication
- Dockerizing a Python ML app with proper layer caching and non-root user setup
- Docker Compose for single-command deployment
