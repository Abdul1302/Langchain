from langchain_huggingface import HuggingFaceEmbeddings

embedding=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',dimensions=32)

text="Delhi is the capital of India"

document=["Delhi is the capital of India",
            "New York is the capital of USA",
            "Paris is the capital of France",
            "Tokyo is the capital of Japan",
            "Beijing is the capital of China"]


vector1=embedding.embed_query(text)

vector2=embedding.embed_documents(document)


print(vector1)

print(vector2)