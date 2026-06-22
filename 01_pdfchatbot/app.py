import streamlit as st
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# We keep Gemini for the chat generation
from langchain_google_genai import ChatGoogleGenerativeAI

# We import HuggingFace for the local embeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables (API Keys)
load_dotenv()

st.title("PDF Question Answering Bot")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    # 1. Save the uploaded file temporarily
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # 2. Load the PDF
    loader = PyPDFLoader(uploaded_file.name)
    documents = loader.load()

    # 3. Split the text into manageable chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)

    # 4. Generate Embeddings locally (This fixes the 429 Quota Error!)
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # 5. Store in FAISS Vector Database
    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )

    # 6. Chat Interface
    question = st.text_input("Ask Question")

    if question:
        # Search the database for relevant chunks
        docs = vector_db.similarity_search(question, k=3)
        context = "\n".join([doc.page_content for doc in docs])

        # Use Gemini to generate the final answer based on the context
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0
        )

        prompt = f"""
        Answer only using the context.

        Context:
        {context}

        Question:
        {question}

        If answer doesn't exist,
        say:

        I could not find the answer in the PDF.
        """

        response = llm.invoke(prompt)

        st.subheader("Answer")
        st.write(response.content)