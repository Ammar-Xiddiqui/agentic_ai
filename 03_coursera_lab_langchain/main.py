# main file 


from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from agent import build_agent

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

agent = build_agent(llm)

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    print(agent.invoke(query))