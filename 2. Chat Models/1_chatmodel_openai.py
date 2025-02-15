from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

#load .env file
load_dotenv()

#initialize the model

#Temperature conrols the randomness of the output. The higher the temperature, the more random the output.

#max_completion_tokensthe number of words or tokens to generate

chat_model=ChatOpenAI(model="gpt-4", temperature=0.9,max_completion_tokens=100) 

#generate the text
result=chat_model.invoke("What is the capital of Pakistan?")

print(result) # Give output with matadata

print(result.content) # Give output without metadata