Retrieval-Augmented Generation (RAG) with Grok API

This project implements a Retrieval-Augmented Generation (RAG) pipeline that extracts and cleans text from PDF documents, splits it into manageable chunks, generates vector embeddings using Sentence-Transformers, stores them in a FAISS index, and uses the Grok API (model: llama-3.1-8B-instant) for intelligent, context-aware text generation.


Features :

    --PDF Extraction – reads and extracts text from PDF files
    --Text Cleaning & Chunking – removes unwanted characters and splits text into logical chunks
    --Vector Embedding Generation – creates embeddings using all-MiniLM-L6-v2 from Sentence-Transformers
    --FAISS Vector Store – stores and retrieves embeddings efficiently
    --Grok API Integration – uses ChatGrok API for generating final responses
    --End-to-End RAG Pipeline – combines retrieval and generation in one flow


Folder Structure

``` RAG/
    │
    ├── .vscode/
    |
    |
    ├── data/
    |   ├──raw/                       # Place your PDFs here
    |   ├── processed/                # chunks.json and cleaned text files are generated automatically here
    │
    ├── src/                          # Contains all Python scripts     
    |   ├── __init__.py               # makes src a package
    │   ├── extraction.py             # Extracts text from PDFs
    │   ├── text_cleaning.py          # Cleans and normalizes text
    │   ├── chunking.py               # Splits text into small chunks
    │   ├── embedding_faiss.py        # Creates embeddings using SentenceTransformer and stores in FAISS
    │   ├── retrieval.py              # Retrieves top matches from FAISS
    │   ├── build.py                  # Handles Grok API communication
    │   ├── config.py                 # Stores paths, constants, API keys
    │ 
    │ 
    ├── vector_store/                 # Auto-created when you run the embedder
    │    ├── my_index.faiss
    │ 
    ├── notebooks/
    │   ├── extraction.ipynb          # jupyter notebook files
    │   ├── text_cleaning.ipynb
    │   . 
    │   .
    │   
    ├── venv/
    │    ├── etc/
    │    ├── include/
    │    .
    │    .
    │ 
    ├── .env.example
    ├── main.py                       # Entry point for querying
    ├── requirements.txt              # Dependencies
    ├── .gitignore
    └── README.md                     # Project documentation
```
