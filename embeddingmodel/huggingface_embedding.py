from langchain_huggingface import HuggingFaceEmbeddings

from dotenv import load_dotenv
load_dotenv()

embedding= HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

texts=[ 
    "hello this is Dhruv Patel",
    "Hello your name is Virat Kohli"
    
]

vector = embedding.embed_documents(texts)
print(vector)