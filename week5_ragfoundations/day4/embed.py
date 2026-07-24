import os
import pickle
from pathlib import Path

import faiss
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter

BASE_DIR = Path(__file__).resolve().parent
DATA_FOLDER = BASE_DIR.parent / "day3" / "papers"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
)

FAISS_INDEX_PATH = "vector_store.faiss"
METADATA_PATH = "metadata.pkl"


#-------------------------------------------------------read Pdf ---------------------------------------------------

def read_pdf(path_to_pdf):
    reader = PdfReader(str(path_to_pdf))

    text = ""
    for page in reader.pages:
        p_text = page.extract_text()

        if p_text:
            text += p_text + "\n"

    return text

#---------------------------------------------chunking-------------------------------------------

def chunk_text(text):

    return text_splitter.split_text(text)

#--------------------------------------------Embedding----------------------------------------

def embed_chunks(chunks):
    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=True,
    )

    return embeddings.astype("float32")


def process_documents():

    all_chunks = []
    metadata = []

    pdf_files = list(Path(DATA_FOLDER).glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found.")
        return None, None

    for pdf in pdf_files:

        print(f"\nProcessing: {pdf.name}")

        text = read_pdf(pdf)

        chunks = chunk_text(text)

        print(f"Created {len(chunks)} chunks")

        for i, chunk in enumerate(chunks):

            all_chunks.append(chunk)

            metadata.append(
                {
                    "source": pdf.name,
                    "chunk_id": i,
                    "text": chunk,
                }
            )

    return all_chunks, metadata


def build_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index



def save_index(index, metadata):

    faiss.write_index(index, FAISS_INDEX_PATH)

    with open(METADATA_PATH, "wb") as f:
        pickle.dump(metadata, f)

    print("\nIndex saved successfully.")



def main():

    chunks, metadata = process_documents()

    if chunks is None:
        return

    print("\nGenerating embeddings...")

    embeddings = embed_chunks(chunks)

    print(f"Generated {len(embeddings)} embeddings")

    print("\nBuilding FAISS index...")

    index = build_faiss_index(embeddings)

    save_index(index, metadata)

    print("\nDone!")
    print(f"Indexed {len(metadata)} chunks.")


if __name__ == "__main__":
    main()
    