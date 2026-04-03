from langchain.agents import create_agent
from agents import llm_openrouter
from prompts import SYSTEM_PROMPT


def create_agents():
    llm_primary = llm_openrouter()
    agent = create_agent(model=llm_primary, tools=[], system_prompt=SYSTEM_PROMPT)

    return agent
