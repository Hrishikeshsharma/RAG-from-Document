import json
import faiss
from sentence_transformers import SentenceTransformer
from src.config import EMBEDDING_MODEL

def create_embedding_store_faiss(input_path:str, output_path:str):

    with open(input_path,"r", encoding="UTF-8") as f:
        chunks = json.load(f)
        
    model = SentenceTransformer(EMBEDDING_MODEL)
    embeddings = model.encode(sentences=chunks, show_progress_bar=True, convert_to_numpy=True)

    dimensions = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimensions)
    index.add(embeddings)
    faiss.write_index(index, output_path)

    print(embeddings.shape)
    print("Number of embeddings in index :", index.ntotal)

if __name__ == "__main__":
    
    input_file = r"C:\Projects\RAG\data\chunks.json"
    output_file = r"C:\Projects\RAG\vector_store\my_index.faiss"
    
    
    