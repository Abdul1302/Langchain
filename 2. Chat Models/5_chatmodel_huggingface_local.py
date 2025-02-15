from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

#Pipleline for the download and use model in local pc

#pipeline_kwargs is a dictionary that contains the parameters for the pipeline
llm=HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.9,
        max_new_tokens=100
    )
)
chat_model=ChatHuggingFace(llm=llm)

result=chat_model.invoke("What is the capital of Pakistan?")

print(result)   