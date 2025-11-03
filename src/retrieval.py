import json
import faiss
import numpy as np
from langchain_groq import ChatGroq
from sentence_transformers import SentenceTransformer
from src.config import GROK_MODEL, GROK_API_KEY

llm = ChatGroq(
    model=GROK_MODEL,
    api_key=GROK_API_KEY
)

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(r"C:\Projects\RAG\vector_store\my_index.faiss")
document_path = r"C:\Projects\RAG\data\processed\chunks.json"

def query_rag(document_path, text):
    
    with open(document_path, "r", encoding="UTF-8") as f:
        documents = json.load(f)
    
    k = 3
    query_vector = model.encode([text])
    query_vector = np.array(query_vector).astype("float32")
    
    distances, indices = index.search(query_vector, k)
    retrieved_docs = [documents[idx] for idx in indices[0]]
    
    context = "\n".join(retrieved_docs)
    prompt = f"Answer the following question based on the context:\n\n{context}\n\nQuestion: {text}\nAnswer:"
    response = llm.invoke(prompt)
    
    print("\n--- Retrieved Context ---\n")
    for i, (idx, dist) in enumerate(zip(indices[0], distances[0])):
        print(f"Rank {i+1} | Distance: {dist:.4f}")
        print(documents[idx], "\n")
    print("\n--- Final Answer ---\n")
    print(response)

text = input("Enter your question: ")
query_rag(document_path, text)
