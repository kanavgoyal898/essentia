import os

DATA_PATH = '../data/'

CHUNK_SIZE = 1024
CHUNK_OVERLAP = 256

# LOADING THE DATA
from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_documents(data_path=DATA_PATH):
    """
    Loads all PDF files from the specified directory.

    Args:
        data_path (str): Directory path containing PDFs (default: DATA_PATH).

    Returns:
        list: Loaded documents.
    """

    files = sorted([file for file in os.listdir(data_path) if file.endswith(".pdf")])
    for file in files:
        print("Indexing `{}` PDF file in {} directory".format(file, data_path))

    document_loader = PyPDFDirectoryLoader(data_path)
    documents = document_loader.load()
    return documents

documents = load_documents()
print(f"Loaded {len(documents):,} documents")
print(f"Sample document: \n{documents[0]}")
print("-------------------")
