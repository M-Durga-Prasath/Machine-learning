from transformers import pipeline


clf = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)

