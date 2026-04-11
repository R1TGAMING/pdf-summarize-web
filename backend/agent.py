from langchain_core.prompts.chat import ChatPromptTemplate
from agents import llm_openrouter, llm_google
from prompts import SYSTEM_PROMPT


def agent():
    llm_primary = llm_google()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", "context:\n{context}\n\nquestion:\n{question}"),
        ]
    )

    chain = prompt | llm_primary
    
    return chain
