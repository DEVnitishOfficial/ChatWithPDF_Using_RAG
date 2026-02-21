from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_path = Path(__file__).parent / "Nodejs_pdf.pdf"

# load this file in the python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

chunks = text_splitter.split_documents(docs)
print(f"Total chunks: {len(chunks)}")
# print the first chunk
# print(f"First chunk: {chunks[0].page_content}")
# print(f"First chunk metadata: {chunks[0].metadata}")
# print(f"second chunk: {chunks[1].page_content}")

print(f"fifty chunk: {chunks[50].page_content}")
print(f"fiftyone chunk: {chunks[51].page_content}")

