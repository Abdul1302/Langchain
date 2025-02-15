from langchain_openai import OpenAI
from dotenv import load_dotenv

#load .env file
load_dotenv()

#initialize the model
llm=OpenAI(model='gpt-3.5-turbo-instruct')

#generate the text
result=llm.invoke("What is the capital of Pakistan?")

print(result)