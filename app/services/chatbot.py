# app/services/chatbot.py

from langchain_postgres import PostgresChatMessageHistory
from langchain.memory import ConversationBufferMemory

def build_memory(session_id: str, conn) -> ConversationBufferMemory:
    history = PostgresChatMessageHistory("chat_history", session_id, sync_connection=conn)
    return ConversationBufferMemory(chat_memory=history, memory_key="chat_history", return_messages=True)


async def run_chat(prompt: str, session_id: str, agent, conn) -> dict:
    memory = build_memory(session_id, conn)

    agent_response = await agent.ainvoke(
        {
            "question": prompt,
            "chat_history": memory.chat_memory.messages
        }
    )

    memory.chat_memory.add_user_message(prompt)

    ai_text = agent_response.get("output", "") if isinstance(agent_response, dict) else str(agent_response)
    memory.chat_memory.add_ai_message(ai_text)

    return {"response": ai_text}


