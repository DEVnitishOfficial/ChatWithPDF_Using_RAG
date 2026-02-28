# ChatWithPDF_Using_RAG

* Installed qdrant vector db using the docker
* see the docker file that how we installed it.
* always run you docker engine first to use the quadrant vector db and run the below command from parent folder wherever is you docker compose file.
* ```docker-compose up -d```
* if you qdrant is up and running check it on localhost:6333 that must appear.

* -qU flag meaning:
    - q : Quiet(Minimizes log output to keep the console clean)
    - U : Upgrade(Ensures you are installing the newest available version)

- Use Poetry to manage dependencies, lock versions and create reproducible installs:

```bash
poetry install        # installs from poetry.lock / pyproject.toml
poetry add <package>  # add a new dependency and update lockfile
poetry run python index.py

## Langchain document loader for PDF 

Installation
Install langchain-community and pypdf.
pip install -qU langchain-community pypdf 
pip freeze > requirements.txt


docs : https://docs.langchain.com/oss/python/integrations/document_loaders/pypdfloader

## Langchain document chunking & splitting

Text splitter integrations
Integrate with text splitters using LangChain.
pip install -U langchain-text-splitters
pip freeze > requirement.txt

docs : https://docs.langchain.com/oss/python/integrations/splitters

## vector embedding

Installation
The LangChain OpenAI integration lives in the langchain-openai package:
pip install -qU langchain-openai

docs: https://docs.langchain.com/oss/python/integrations/text_embedding/openai


## install langchain_qdrant using which we can talk to our qdrant db(it's a bridge b/w langchain and qdrant vector db)

Qdrant integration
Integrate with the Qdrant vector store using LangChain Python.
pip install -qU langchain-qdrant

docs: https://docs.langchain.com/oss/python/integrations/vectorstores/qdrant

