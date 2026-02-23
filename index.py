from dotenv import load_dotenv

from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

load_dotenv() # load environment variables from .env file

pdf_path = Path(__file__).parent / "Nodejs_pdf.pdf"

# load this file in the python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()

# split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

chunks = text_splitter.split_documents(docs)
print(f"Total chunks: {len(chunks)}")

# create vector embeddings for the chunks

# Here embedding model will take those created chunks and then it will store
# in the qdrant database(vector db) and then we can query that database to get 
# the relevant chunks based on the query
embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")

# install langchain_qdrant package to use Qdrant vector database(works 
# like bridge between langchain and qdrant)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embeddings_model,
    url="http://localhost:6333", # open you localhost:6333/dashboard to see the qdrant dashboard
    collection_name="my_first_rag_collection" # name of the collection in qdrant database where the chunks will be stored,
)

print("Vector store created and chunks stored in Qdrant database successfully!")
print("Indexing completed.")