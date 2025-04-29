from langchain_ollama import ChatOllama
from app.services.tools.get_current_time import get_current_time
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


def create_chat_assistant(llm: ChatOllama):
    tools = [get_current_time]
    prompt = ChatPromptTemplate.from_messages([
        ("system",
        """
        Você é um assistente de IA educado, inteligente e prestativo.

        Seu objetivo principal é responder às perguntas dos usuários com base no seu próprio conhecimento.

        Você possui acesso a ferramentas externas que podem ser usadas APENAS se for estritamente necessário.

        Instruções:
        - Se souber a resposta, responda diretamente, com naturalidade e sem mencionar ferramentas ou processos internos.
        - Só chame uma ferramenta se realmente precisar.
        - Nunca explique ou diga que vai usar ou não vai usar uma ferramenta.
        - O usuário nunca deve saber sobre seu processo de pensamento interno.

        Seja direto, natural e humano na conversa.
        """
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{question}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(
        llm=llm,
        tools=tools,
        prompt=prompt
    )

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        handle_parsing_errors=True
    )

    return agent_executor


