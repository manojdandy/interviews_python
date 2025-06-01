import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time

from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
print(os.getenv("GROQ_API_KEY"))
#llm=ChatGroq(model="qwen-qwq-32b")
#gemma2-9b-it
llm_model="llama3"
llm_model="gemma2-9b-it"
llm=ChatGroq(model="gemma2-9b-it")
print(llm.invoke("what is the capital of india"))


if "vector_db" not in st.session_state:
    st.session_state.embeddings = OllamaEmbeddings(model="llama3")
    st.session_state.loader=WebBaseLoader(["https://langchain-ai.github.io/langgraph/"])
    st.session_state.docs = st.session_state.loader.load()
    st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
    st.session_state.vector_db = FAISS.from_documents(documents=st.session_state.final_documents,embedding=st.session_state.embeddings)

st.title("Chat GroQ Demo")
prompt = ChatPromptTemplate.from_template(
    """
        Answer the questions based on provided context only 
        Please provide the response based on most accurate context
        <context>
        {context}
        </context>
        Questions : {input}
    """
)

document_chain = create_stuff_documents_chain(llm,prompt=prompt)
retriever = st.session_state.vector_db.as_retriever()
retriever_chain = create_retrieval_chain(retriever,document_chain)
prompt = st.text_input(("input your prompt here"))

if prompt:
    start = time.process_time()
    response = retriever_chain.invoke({"input":prompt})
    print("Reponse time :: ", time.process_time() - start)
    st.write(response['answer'])
    #with a streamlit expander
    with st.expander("Document similarity search"):
        #find the relvenat chunks
        for i,doc in enumerate(response['context']):
            st.write(doc.page_content)
            st.write("---------")

#streamlit run app.py


