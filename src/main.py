import os
import subprocess

from train import get_embedding_function
from constants import *

# RUNNING RAG LOCALLY
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

if not os.path.exists(CHROMA_PATH):
    try:
        subprocess.run(["python3", "train.py"], check=True)
    except subprocess.CalledProcessError:
        print(f"Error running train.py, aborting.")
        exit(1)

def query_rag(query_text: str):
    embedding_function = get_embedding_function()
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_function,
    )

    results = db.similarity_search(query_text, k=K)

    context_text = "\n\n---\n\n".join([result.page_content for result in results])
    sources = set([f"{result.metadata.get('source', 'UNKNOWN')} :: page: {result.metadata.get('page', 'UNKNOWN')}" for result in results])
    
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = ChatOllama(model=LLM_MODEL_NAME)
    response = model.invoke(prompt)
    answer = response.content

    return answer, sources

query_text = input("QUESTION: ")
answer, sources = query_rag(query_text)

print("______________________")
print(f"ANSWER:\n{answer}\n")
print(f"SOURCES:")
for source in sources:
    print(f"    - {source}")
