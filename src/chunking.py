import re
import json
from langchain_text_splitters import RecursiveCharacterTextSplitter


def clean_text_for_splitting(text: str) -> str:
    text = re.sub(r'^[^\w]+', '', text, flags=re.MULTILINE)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def split_text_into_chunks(input_path: str, output_path: str, chunk_size=500, chunk_overlap=100):
    with open(input_path, "r", encoding="UTF-8") as f:
        text = f.read()

    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    text_string = "\n".join(sentences)
    text_string = clean_text_for_splitting(text_string)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", ". ", "! ", "? ", " "]
    )

    chunks = text_splitter.split_text(text_string)
    chunks = [re.sub(r'^[^\w]+', '', t).strip() for t in chunks]
    chunks = [chunk + "." if not chunk.endswith(".") else chunk for chunk in chunks]

    with open(output_path, "w", encoding="UTF-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    print(f"{len(chunks)} chunks saved to {output_path}")


if __name__ == "__main__":
    input_file = r"C:\Projects\RAG\data\text_cleaned.txt"
    output_file = r"C:\Projects\RAG\data\chunks.json"
    
    split_text_into_chunks(input_file, output_file)
