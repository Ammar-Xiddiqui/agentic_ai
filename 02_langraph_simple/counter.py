from typing import TypedDict
from langgraph.graph import StateGraph, END
import random
import string


# -------------------------
# State Definition
# -------------------------
class ChainState(TypedDict):
    n: int
    letter: str


# -------------------------
# Node 1: Increment Counter
# -------------------------
def add(state: ChainState) -> ChainState:
    random_letter = random.choice(string.ascii_lowercase)

    return {
        **state,
        "n": state["n"] + 1,
        "letter": random_letter,
    }


# -------------------------
# Node 2: Print State
# -------------------------
def print_out(state: ChainState) -> ChainState:
    print(
        f"Current n: {state['n']} | "
        f"Letter: {state['letter']}"
    )
    return state


# -------------------------
# Stop Condition
# -------------------------
def stop_condition(state: ChainState) -> bool:
    return state["n"] >= 13


# -------------------------
# Build Workflow
# -------------------------
workflow = StateGraph(ChainState)

workflow.add_node("add", add)
workflow.add_node("print", print_out)

workflow.set_entry_point("add")

workflow.add_edge("add", "print")

workflow.add_conditional_edges(
    "print",
    stop_condition,
    {
        True: END,
        False: "add",
    }
)

# -------------------------
# Compile Graph
# -------------------------
app = workflow.compile()


# -------------------------
# Run Graph
# -------------------------
result = app.invoke(
    {
        "n": 1,
        "letter": ""
    }
)

print("\nFinal State:")
print(result)