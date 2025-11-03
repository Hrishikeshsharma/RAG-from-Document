from src.extraction import text_extraction
from src.text_cleaning import clean_text_file
from src.chunking import split_text_into_chunks
from src.embedding_faiss import create_embedding_store_faiss

document_pdf = r"C:\Projects\RAG\data\raw\yuval_noah_harari-sapiens_a_brief_histor.pdf"
extracted_text = r"C:\Projects\RAG\data\raw\text_uncleaned.txt"
cleaned_text = r"C:\Projects\RAG\data\processed\text_cleaned.txt"
chunks = r"C:\Projects\RAG\data\processed\chunks.json"
vector_db = r"C:\Projects\RAG\vector_store\my_index.faiss"

text_extraction(input_path=document_pdf, output_path=extracted_text)
clean_text_file(input_path=extracted_text, output_path=cleaned_text)
split_text_into_chunks(input_path=cleaned_text, output_path=chunks)
create_embedding_store_faiss(input_path=chunks, output_path=vector_db)
