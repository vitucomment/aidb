# app/services/chatbot.py

from langchain_postgres import PostgresChatMessageHistory
from langchain.memory import ConversationBufferMemory

def build_memory(session_id: str, conn) -> ConversationBufferMemory:
    history = PostgresChatMessageHistory(
        "chat_history",  # positional
        session_id,
        sync_connection=conn
    )

    return ConversationBufferMemory(
        chat_memory=history,
        memory_key="chat_history",
        return_messages=True
    )


async def run_chat(prompt: str, session_id: str, agent, conn) -> dict:
    memory = build_memory(session_id, conn)

    response = await agent.ainvoke(
        {
            "question": prompt,
            "chat_history": memory.chat_memory.messages
        }
    )
    return {"response": response}