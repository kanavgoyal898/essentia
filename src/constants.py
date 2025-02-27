DATA_PATH = '../data/'
CHROMA_PATH = '../database/'

CHUNK_SIZE = 1024
CHUNK_OVERLAP = 256
BATCH_SIZE = 16

MODEL_NAME = 'llama3'

K = 5
PROMPT_TEMPLATE = '''
    Answer the question based only on the following context:
    CONTEXT:
    {context}
    \n\n\n\n
    QUESTION:
    {question}
'''
