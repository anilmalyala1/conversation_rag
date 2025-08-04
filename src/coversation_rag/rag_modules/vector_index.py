from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import find_dotenv,load_dotenv



def create_index(docs, persist_dir):
    load_dotenv(find_dotenv())
    print("Into create index ---->")
    db = Chroma.from_documents(docs, OpenAIEmbeddings())
    db.persist()

def load_index(persist_dir):
    load_dotenv(find_dotenv())
    print("Into load index ---->")
    return Chroma(embedding_function=OpenAIEmbeddings())
