from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

document=["Delhi is the capital of India",
            "New York is the capital of USA",
            "Paris is the capital of France",
            "Tokyo is the capital of Japan",
            "Beijing is the capital of China"]

result=embedding.embed_documents   ("Delhi is the capital of India")

print(result)