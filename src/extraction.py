from PyPDF2 import PdfReader

def text_extraction(input_path, output_path):

    reader = PdfReader(input_path)
    no_of_pages = len(reader.pages)
    print(f"{no_of_pages} pages extracted.")
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    with open(output_path, "w", encoding="UTF-8") as f:
        f.write(text)
        
if __name__ == "__main__":
    
    input_file = r"C:\Projects\RAG\data\yuval_noah_harari-sapiens_a_brief_histor.pdf"
    output_file = r"C:\Projects\RAG\data\text_uncleaned.txt"
        
    text_extraction(input_file, output_file)