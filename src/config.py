import os
from dotenv import load_dotenv

load_dotenv()


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
DATA_PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
VECTOR_STORE_PATH = os.path.join(BASE_DIR, "vector_store", "my_index.faiss")

EMBEDDING_MODEL = "all-MiniLM-L6-v2"


GROK_API_KEY = os.getenv("GROK_API_KEY")
GROK_MODEL = os.getenv("GROK_MODEL", "llama-3.1-8B-instant")
GROK_API_URL = "https://api.x.ai/v1/chat/completions"  # Example endpoint (adjust if needed)


CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

DEBUG = True 
