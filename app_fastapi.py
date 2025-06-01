#how to run ? uvicorn app_fastapi:app --reload
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from contextlib import asynccontextmanager
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
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.output_parsers import StrOutputParser


# GLOBAL VARIABLES
vector_db = None
retriever_chain = None


# Lifespan function for startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    global vector_db,retriever_chain
    # 🎯 Startup code here
    print("🚀 Server is starting up...")
    load_dotenv()
    # e.g., Load vector db, embeddings, models
    embeddings = OllamaEmbeddings(model="llama3")
    llm = ChatOllama(model="llama3")
    #llm = ChatGroq(model="qwen-qwq-32b")
    loader = WebBaseLoader(["https://langchain-ai.github.io/langgraph/"])
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    documents = text_splitter.split_documents(docs)
    vector_db = FAISS.from_documents(documents=documents,embedding=embeddings)
    retriever = vector_db.as_retriever()
    #create the prompt
    prompt_template = ChatPromptTemplate.from_template("""
    Answer the question based on provided context only
                                                <context>
                                                {context}
                                                </context>
                                              Question : {input}
                                              """)
    
    # wrap the retriever 
    retriever_chain = (
        {"context":retriever,"input":RunnablePassthrough()}
        | prompt_template
        | llm
        | StrOutputParser()
    )
    #document_chain = create_stuff_documents_chain(llm,prompt=prompt_template)
    #retriever_chain = create_retrieval_chain(retriever,document_chain)
    yield
    # 🎯 Shutdown code here
    print("👋 Server is shutting down...")

app = FastAPI(lifespan=lifespan)


# Pydantic model for request body
class QueryRequest(BaseModel):
    prompt: str

@app.post("/chat")
async def chat_with_groq(request:QueryRequest):
    global retriever_chain
    print(f"request : {request.prompt}")
    if retriever_chain is None:
        return {"error":"system is not ready yet"}
    #invoke the 
    response = retriever_chain.invoke(request.prompt)
    print(f"response :: {response}")
    #return {"answer":response['answer']}
    return {"answer":response}

# Serve the HTML form for user input
@app.get("/", response_class=HTMLResponse)
async def get_input_form():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LangChain Chat</title>
    </head>
    <body>
        <form id="chat-form">
            <input type="text" id="user-input" name="user-input" placeholder="Ask a question..." required>
            <button type="submit">Submit</button>
        </form>
        <p id="response"></p>

        <script>
            document.getElementById('chat-form').addEventListener('submit', async function(event) {
                event.preventDefault();
                const userInput = document.getElementById('user-input').value;

                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ prompt: userInput }),
                });

                const data = await response.json();
                document.getElementById('response').textContent = 'Answer: ' + data.answer;
            });
        </script>
    </body>
    </html>
    """



