from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from dotenv import find_dotenv,load_dotenv

def run_query(vectorstore, question):
   # pipe = pipeline("text-generation", model="bigcode/starcoder", max_new_tokens=512)
   # llm = HuggingFacePipeline(pipeline=pipe)
    load_dotenv(find_dotenv())


    llm = ChatOpenAI(model="gpt-4", temperature=0)


    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return qa.run(question)
