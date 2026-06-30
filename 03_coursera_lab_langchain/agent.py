from langchain.agents import Tool, initialize_agent, AgentType
from tools import calculate_power

power_tool = Tool(
    name="Power Tool",
    func=calculate_power,
    description="Calculate x raised to y."
)

def build_agent(llm):
    return initialize_agent(
        tools=[power_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )