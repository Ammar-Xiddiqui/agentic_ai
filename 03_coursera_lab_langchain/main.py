from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from tools import calculate_power,multiply

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)

agent = create_agent(
    model=llm,
    tools=[calculate_power,multiply],
    system_prompt="You are a helpful math assistant."
)

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ]
        }
    )

    print(response["messages"][-1].content)