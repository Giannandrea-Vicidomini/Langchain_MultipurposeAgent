import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import (
    create_tool_calling_agent,
    AgentExecutor,
    create_react_agent,
)
from tools.youtube_tools import search_youtube_tool
from tools.util_tools import save_user_input
from langchain import hub


_ = load_dotenv(find_dotenv())


def initialize_agent():

    llm = ChatOpenAI(temperature=0.5, model=os.getenv("MODEL_OPENAI"))
    tools = [search_youtube_tool,save_user_input]

    # prompt = hub.pull("hwchase17/openai-functions-agent") --- NON USARE

    prompt = hub.pull(
        "hwchase17/react"
    )  # questo prompt funziona solo con create react agent, altrimetni da errore se lo si da al create tool calling agent
    # agent = create_tool_calling_agent(llm,tools,prompt) --- NON USARE
    agent = create_react_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor
