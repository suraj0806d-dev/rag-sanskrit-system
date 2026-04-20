# rag-sans# Sanskrit RAG System (CPU-Based)

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system for Sanskrit documents using CPU-only inference.

## Features
- Sanskrit document ingestion (.txt)
- Text preprocessing and chunking
- FAISS-based vector retrieval
- Query answering system
- CPU-efficient pipeline

## Tech Stack
- Python
- LangChain
- FAISS
- NumPy

## How it works
1. Load Sanskrit documents
2. Split into chunks
3. Convert to embeddings
4. Store in FAISS vector DB
5. Retrieve relevant chunks
6. Generate response

## Run the project
```bash
pip install -r requirements.txt
python src/main.pykrit-system
