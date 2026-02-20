from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

def main():
    pdf_path = Path(__file__).parent.parent / "Nodejs_pdf.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    docs = loader.load()
    print(docs[12])

if __name__ == "__main__":
    main()
