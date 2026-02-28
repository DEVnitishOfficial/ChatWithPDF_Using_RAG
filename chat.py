from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()  # load environment variables from .env file

openai_client = OpenAI()


embeddings_model = OpenAIEmbeddings(model="text-embedding-3-large")


vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",  
    collection_name="my_first_rag_collection",
    embedding=embeddings_model,
)

# Take user query as input

user_Query = input("ask question that you want to know about the document: ")


# Relevent chunks from the vector database based on the user query
search_results = vector_db.similarity_search(
    query=user_Query, k=3
)  # k is the number of relevant chunks you want to retrieve

context = "\n\n\n".join(
    [
        f" page content :{result.page_content}\n page number :{result.metadata['page_label']}\n file location :{result.metadata['source']}"
        for result in search_results
    ]
)

SYSTEM_PROMPT = """

You are a helpful assistant that answers questions based on the available context. 
you should use only the provided context to answer the question, and navigate the user to open the correct page number in the document to find the answer and learn more about the topic.

context:
{context}
"""

response = openai_client.chat.completions.create(
    model="gpt-5.2",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT.format(context=context),
        },
        {"role": "user", "content": user_Query},
    ],
)

print(f"Answer 🤖 : {response.choices[0].message.content}")