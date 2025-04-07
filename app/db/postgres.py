from langchain_community.chat_message_histories import PostgresChatMessageHistory
from langchain.memory import ConversationBufferMemory
import psycopg
from langchain_postgres import PostgresChatMessageHistory

POSTGRES_CONN = "postgresql://postgres:innersql@172.20.116.5:5432/postgres"
CHAT_TABLE = "chat_history"


def get_memory(session_id: str) -> ConversationBufferMemory:
    history = PostgresChatMessageHistory(
        session_id=session_id,
        connection_string=POSTGRES_CONN,
    )
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        chat_memory=history,
    )
    return memory


def init_psycopg_connection():
    return psycopg.connect(POSTGRES_CONN)

def create_chat_history_table(conn):
    PostgresChatMessageHistory.create_tables(conn, CHAT_TABLE)
