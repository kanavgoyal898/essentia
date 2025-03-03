# essentiCall: Document-Retrieval-Augmented Generator

essentiCall is a Retrieval-Augmented Generation (RAG) application that enables users to query information from a collection of PDF documents. It leverages document loading, text chunking, embeddings, and a vector database to provide relevant answers to user queries using a language model.

<div>
  <img src="./image.jpg" alt="Preview">
</div>

## Features
- **Automatic PDF Processing**: Load and process PDF files from a specified directory.
- **Text Chunking**: Splits documents into smaller chunks for efficient retrieval.
- **Vector Embeddings**: Uses a pre-trained model to generate document embeddings.
- **ChromaDB Integration**: Stores and retrieves document embeddings using Chroma.
- **Question Answering**: Retrieves relevant information and generates responses using a language model.

## Installation
### Prerequisites
Ensure you have Python 3.8+ installed and the required dependencies.

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/kanavgoyal898/essentiCall.git
   cd essentiCall
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### Training Phase (Indexing PDFs)
Run the following command to process and index PDFs:
```sh
cd src/
python train.py
```
This script:
- Loads PDFs from the specified directory.
- Splits them into smaller chunks.
- Computes embeddings and stores them in ChromaDB.

### Querying Information
To ask questions based on the indexed documents, run:
```sh
cd src/
python main.py
```
You will be prompted to enter a question. The system will retrieve relevant document chunks and generate an answer.

## Configuration
Modify `constants.py` to customize:
- `DATA_PATH`: Path to the directory containing PDFs.
- `CHUNK_SIZE` and `CHUNK_OVERLAP`: Control document chunking.
- `EMB_MODEL_NAME`: Name of the embedding model.
- `LLM_MODEL_NAME`: Name of the large language model.
- `CHROMA_PATH`: Directory for storing the ChromaDB index.
- `K`: Number of retrieved chunks per query.
- `PROMPT_TEMPLATE`: Defines the format for querying the language model.

## Dependencies
Install all dependencies using:
```sh
pip install -r requirements.txt
```

## Examples

```sh
QUESTION: What is physics?
______________________
ANSWER:
Physics is the most fundamental and all-inclusive of the sciences, and has had a profound effect on all scientific development. It is the present-day equivalent of what used to be called "natural philosophy", from which most of our modern sciences arose.

SOURCES:
    - ../data/The Feynman Lectures on Physics, Vol. 1.pdf :: page: 76
    - ../data/The Feynman Lectures on Physics, Vol. 1.pdf :: page: 50
    - ../data/The Feynman Lectures on Physics, Vol. 1.pdf :: page: 67
    - ../data/The Feynman Lectures on Physics, Vol. 1.pdf :: page: 81
```

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.
