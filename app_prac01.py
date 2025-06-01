#how to run ? uvicorn app_fastapi:app --reload
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_ollama.chat_models import ChatOllama
from langchain_groq.chat_models import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import create_retrieval_chain
from langchain_core.runnables import RunnablePassthrough,RunnableMap
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

# GLOBAL VARIABLES
vector_db = None
retriever_chain = None


def format_docs(docs):
    return "\n\n".join([d.page_content for d in docs])

def test_func():
    load_dotenv()
    embeddings = OllamaEmbeddings(model="llama3")
    loader = WebBaseLoader(["https://langchain-ai.github.io/langgraph/"])
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    final_documents = text_splitter.split_documents(docs)
    vector_db = FAISS.from_documents(documents=final_documents, embedding=embeddings)

    retriever = vector_db.as_retriever()

    llm = ChatGroq(
        model="qwen-qwq-32b"
    )

    # Create the prompt
    prompt_template = ChatPromptTemplate.from_template(
        """
        Answer the questions based on provided context only.
        Please provide the response based on the most accurate context.
        <context>
        {context}
        </context>
        Question: {question}
        """
    )

    
    # Now manually wire up the retrieval chain using Runnables
    retriever_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}  # Pass the user input
        | prompt_template  # Apply the prompt
        | llm  # Use the Groq model for response
        #| StrOutputParser()
    )

    response = retriever_chain.invoke("what is langgraph")
    print(response)
    #print(llm.invoke("what is captial of india"))


if __name__=="__main__":
    test_func()