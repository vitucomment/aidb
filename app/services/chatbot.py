def run_chat(prompt: str, agent) -> dict:
    response = agent.invoke({"question": prompt})
    return {"response": response}
