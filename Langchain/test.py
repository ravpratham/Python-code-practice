import os
import langchain
from langchain import HuggingFaceHub

def HuggingFaceTest(query):
    os.environ["HUGGINGFACEHUB_API_TOKEN"]   = "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"

    llm_huggingface = HuggingFaceHub(repo_id = "google/flan-t5-large",model_kwargs={"temperature":0.5 ,"max_length":64})
    query =  "translate this sentence to german : i am pratham"
    output  = llm_huggingface.predict(query)
    return output
prompt = input("WHAT DO YOU WANT TO ASK - ")
print(HuggingFaceTest(prompt))

def Llama2Test():
    pass

