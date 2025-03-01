parameters = {
    'nomic-embed-text': {
        'chunk_size': 1024,
        'chunk_overlap': 256,
    },
    'llama3': {
        'chunk_size': 4096,
        'chunk_overlap': 1024,
    },
}

EMB_MODEL_NAME = 'nomic-embed-text'
LLM_MODEL_NAME = 'llama3'

CHUNK_SIZE = parameters[EMB_MODEL_NAME]['chunk_size']
CHUNK_OVERLAP = parameters[EMB_MODEL_NAME]['chunk_overlap']
BATCH_SIZE = 16

DATA_PATH = '../data/'
CHROMA_PATH = f'../database/{EMB_MODEL_NAME}/'

K = 5
PROMPT_TEMPLATE = '''
Answer the question based only on the following context:
Context:
{context}
\n\n\n\n
Question:
{question}
'''
