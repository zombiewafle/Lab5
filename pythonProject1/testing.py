import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
load_dotenv()

# Initialize Pinecone
api_key = os.getenv("PINECONE_API_KEY")
if api_key is None:
    raise ValueError("PINECONE_API_KEY is not set in environment variables")

pc = Pinecone(api_key=api_key)

# Define and connect to an existing index or create a new one
index_name = "langchain-helper-index"
if index_name in pc.list_indexes().names():
    pc.delete_index(name=index_name)
    print(f"Deleted existing index: {index_name}")

pc.create_index(
    name=index_name,
    dimension=768,  # Ensure dimension is correct
    metric='cosine',  # Using cosine similarity
    spec=ServerlessSpec(
        cloud='aws',
        region='us-east-1'  # Use a supported region
    )
)
print(f"Created new index with dimension 768: {index_name}")

# Connect to the newly created index
index = pc.Index(name=index_name)

# Insert some vectors
vectors = {
    "id1": ([0.5]*768, {"metadata": "value1"}),
    "id2": ([0.6]*768, {"metadata": "value2"})
}
index.upsert(vectors=vectors)
print("Inserted vectors into the index.")

# Query the index
try:
    query_vector = [0.5]*768  # A simple uniform vector
    query_results = index.query(queries=[query_vector], top_k=2)
    print("Query Results:", query_results)
except Exception as e:
    print("Failed to query the index:", str(e))

# Close the Pinecone connection
pc.close()
