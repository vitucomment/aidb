from datetime import datetime
from langchain_core.tools import tool

@tool
def get_current_time() -> str:
    """Retorna a hora atual formatada no horário local."""
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
