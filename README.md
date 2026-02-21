# ChatWithPDF_Using_RAG

* Installed qdrant vector db using the docker
*  
*  

- Use Poetry to manage dependencies, lock versions and create reproducible installs:

```bash
poetry install        # installs from poetry.lock / pyproject.toml
poetry add <package>  # add a new dependency and update lockfile
poetry run python index.py

## Langchain document loader for PDF 

Installation
Install langchain-community and pypdf.
pip install -qU langchain-community pypdf 
pip freeze > requirement.txt


docs : https://docs.langchain.com/oss/python/integrations/document_loaders/pypdfloader

## Langchain document chunking & splitting

Text splitter integrations
Integrate with text splitters using LangChain.
pip install -U langchain-text-splitters
pip freeze > requirement.txt

docs : https://docs.langchain.com/oss/python/integrations/splitters