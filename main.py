from src.retrieval import query_rag

chunks = r"C:\Projects\RAG\data\processed\chunks.json"
vector_db = r"C:\Projects\RAG\vector_store\my_index.faiss"

while True:
    question = input("\nEnter your question (or type 'exit' to quit): ")
    if question.lower() == "exit":
        print("Exiting...")
        break
    query_rag(document_path=chunks, text=question)
