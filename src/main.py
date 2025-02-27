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

# SPLIT THE DOCUMENTS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document

def split_documents(documents: list[Document], chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    """
    Splits documents into smaller chunks.

    Args:
        documents (list[Document]): List of documents to split.
        chunk_size (int): Size of each chunk (default: CHUNK_SIZE).
        chunk_overlap (int): Overlap between chunks (default: CHUNK_OVERLAP).

    Returns:
        list: List of document chunks.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        is_separator_regex=False
    )

    splits = text_splitter.split_documents(documents)
    return splits

chunks = split_documents(documents)
print(f"Split {len(documents):,} documents into {len(chunks):,} chunks")
print(f"Sample chunk: \n{chunks[0]}")
print("-------------------")
