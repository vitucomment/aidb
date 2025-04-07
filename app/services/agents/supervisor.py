from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

def create_chat_assistant(llm: ChatOllama):
    prompt = ChatPromptTemplate.from_template(
        "You are a helpful and smart assistant. Respond to the following user message:\n\n{question}"
    )
    chain = prompt | llm
    return chain
