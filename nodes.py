from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from react import llm,tools
load_dotenv()

SYSTEM_MESSAGE = """
You are a helpful assistant that can use tools to answer the questions.
"""

def run_agent_reasoning(state: MessagesState) -> MessagesState:
    response = llm.invoke(
        [
            {"role": "system", "content": SYSTEM_MESSAGE},
            *state["messages"]
        ]
    )
    return {"messages": [response]}

tools_node = ToolNode(tools)