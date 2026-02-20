from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

pdf_path = Path(__file__).parent / "Nodejs_pdf.pdf"

# load this file in the python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# print the content of the file
print(docs[12])