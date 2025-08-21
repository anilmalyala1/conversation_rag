from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_java_repo(repo_path: str):
    loader = DirectoryLoader(path=repo_path, glob="**/*.java", loader_cls=TextLoader)
    docs = loader.load()
    print(len(docs))
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(docs)
