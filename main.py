import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA

# Load document
loader = TextLoader("sample.txt")
docs = loader.load()

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10)
chunks = splitter.split_documents(docs)

# Embedding and vector DB
api_key = os.getenv("OPENAI_API_KEY")
embeddings = OpenAIEmbeddings(openai_api_key=api_key)
db = FAISS.from_documents(chunks, embeddings)

# Set up retriever + LLM
retriever = db.as_retriever()
llm = OpenAI(openai_api_key=api_key)
qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Ask user
query = input("Ask a question about the document: ")
print("\nAnswer:", qa.run(query))
