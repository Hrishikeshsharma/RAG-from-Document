import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords", quiet=True)

def clean_text(text: str) -> str:

    text = text.replace('\x0c', ' ')                            # remove unwanted form-feed chars
    text = re.sub(r'[\t\r\f\v]+', ' ', text)                    # remove page breaks/tabs
    text = re.sub(r'\s+', ' ', text)                            # collapse multiple spaces
    text = re.sub(r'Page\s*\d+', '', text, flags=re.IGNORECASE) # remove page numbers like "Page 3"
    text = text.strip().lower()
    return text

def clean_text_file(input_path: str, output_path: str) -> None:

    with open(input_path, "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned_text = clean_text(raw_text) # calling th function

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(f"Cleaned text saved to {output_path}")

if __name__ == "__main__":

    input_file = r"C:\Projects\RAG\data\text_uncleaned.txt"
    output_file = r"C:\Projects\RAG\data\text_cleaned.txt"

    clean_text_file(input_file, output_file)

# input file and output file are arguments to the clean_text_file function
# input_file --> input_path
# out_file --> output_path