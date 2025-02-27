import os
from tqdm import tqdm
from multiprocessing import cpu_count
from constants import *

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
    print()

    document_loader = PyPDFDirectoryLoader(data_path)
    documents = document_loader.load()
    return documents

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

# EMBEDDING FUNCTION
from langchain_ollama import OllamaEmbeddings

def get_embedding_function(model_name=MODEL_NAME):
    """
    Returns an embedding function using the specified model.
    
    Args:
        model_name (str): Name of the embedding model (default: MODEL_NAME).
    
    Returns:
        OllamaEmbeddings: Embedding function instance.
    """

    embeddings = OllamaEmbeddings(
        model=model_name,
    )
    return embeddings

# CREATING THE DATABASE
from langchain_chroma import Chroma

def add_to_chroma(chunks: list[Document], embedding_function=None):
    """
    Adds document chunks to a Chroma vector database.

    Args:
        chunks (list[Document]): List of document chunks to store.
        embedding_function (callable, optional): Function returning an embedding model. 
                                                 Defaults to get_embedding_function().
    
    Returns:
        Chroma: The Chroma vector database instance.
    """

    if not chunks:
        print("Warning: No chunks to add to the database.")
        return None
    
    if not embedding_function:
        embedding_function = get_embedding_function()
        
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_function,
    )

    print("Adding chunks to ChromaDB...")

    batch_size = BATCH_SIZE
    for i in tqdm(range(0, len(chunks), batch_size), desc="Processing chunks", unit="batch"):
        db.add_documents(chunks[i:i+batch_size])

    print("Database saved successfully.")

    return db

def main():
    documents = load_documents()
    print(f"Loaded {len(documents):,} documents")
    print(f"Sample document: \n{documents[0]}")
    print("-------------------\n")

    chunks = split_documents(documents)
    print(f"Split {len(documents):,} documents into {len(chunks):,} chunks")
    print(f"Sample chunk: \n{chunks[0]}")
    print("-------------------\n")

    embedding_function = get_embedding_function()
    print(f"Sample embedding function: \n{embedding_function}")
    print("-------------------\n")

    db = add_to_chroma(chunks)
    print(f"Sample database: \n{db}")
    print("-------------------\n")

if __name__ == "__main__":
    main()
