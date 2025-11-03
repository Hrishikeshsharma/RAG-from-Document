**Retrieval-Augmented Generation (RAG) with Grok API**

This project implements a Retrieval-Augmented Generation (RAG) pipeline that extracts and cleans text from PDF documents, splits it into manageable chunks, generates vector embeddings using Sentence-Transformers, stores them in a FAISS index, and uses the Grok API (model: llama-3.1-8B-instant) for intelligent, context-aware text generation.


**Features :**

    --PDF Extraction – reads and extracts text from PDF files
    --Text Cleaning & Chunking – removes unwanted characters and splits text into logical chunks
    --Vector Embedding Generation – creates embeddings using all-MiniLM-L6-v2 from Sentence-Transformers
    --FAISS Vector Store – stores and retrieves embeddings efficiently
    --Grok API Integration – uses ChatGrok API for generating final responses
    --End-to-End RAG Pipeline – combines retrieval and generation in one flow

**Setup and Installation**

    Follow the steps below to set up and run this project locally.

1. Clone the repository
--------------------------
    git clone https://github.com/Hrishikeshsharma/RAG-from-Document.git
    cd RAG-from-Document

2. Create a virtual environment
--------------------------------
    python -m venv venv

3. Activate the virtual environment
-------------------------------------
    Windows:
    venv\Scripts\activate

    macOS/Linux:
    source venv/bin/activate

4. Install dependencies
-------------------------
    pip install -r requirements.txt

5.  Add your PDF files
-------------------------
    Place all your source PDF files inside:
    data/raw/

6.  Build the RAG index
-------------------------
    Run the following command to extract text, clean it, chunk it, and create embeddings:
    python src/build_rag.py

    This will automatically generate:
    data/processed/chunks.json
    vector_store/my_index.faiss

7.  Run the application
------------------------
    After building the index, start the interactive question-answer interface:
    python main.py

    You can then type your questions directly in the terminal, for example:
    Question: What is evolution?
8.  Environment variables (if required)
-----------------------------------------
    If your project requires API keys (for example, Groq or OpenAI), create a .env file in the project root and add your keys:
    GROQ_API_KEY=your_api_key_here

**Folder Structure**

> **Note:** Some folders (like `venv/`, `data/raw/`, `vector_store/`) are listed here for structure clarity but are **excluded via `.gitignore`**.


``` RAG/
    │
    ├── .vscode/
    │ 
    │ 
    ├── data/
    │   ├──raw/                       # Place your PDFs here
    │   ├── processed/                # chunks.json and cleaned text files are generated automatically here
    │
    ├── src/                          # Contains all Python scripts     
    │   ├── __init__.py               # makes src a package
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
