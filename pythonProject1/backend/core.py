import os
from dotenv import load_dotenv
from typing import Any
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from pinecone import Pinecone
from langchain_community.vectorstores import Pinecone as PineconeLangChain

load_dotenv()

# Initialize Pinecone with API key
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])


def run_llm(query: str) -> Any:
    # Ensure you use the same model for embeddings used during document ingestion
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # Retrieve the existing Pinecone index
    doc_search = PineconeLangChain.from_existing_index(
        index_name=os.environ["INDEX_NAME"],  # Ensure this is correctly set in your .env file
        embedding=embeddings
    )

    # Initialize the Chat component
    chat = ChatOpenAI(verbose=True, temperature=0)

    # Set up retrieval-based QA system
    qa = RetrievalQA.from_chain_type(
        llm=chat,
        chain_type="stuff",  # Ensure this is set to a meaningful type or adjusted as needed
        retriever=doc_search.as_retriever(),
        return_source_documents=True
    )

    # Run the query and return the result
    return qa({"query": query})


if __name__ == "__main__":
    result = run_llm("What is LangChain?")
    print(result)
