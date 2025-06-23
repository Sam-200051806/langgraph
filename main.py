from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph,MessagesState,END
from nodes import run_agent_reasoning,tools_node
load_dotenv()

AGENT_REASON = "yaha se shuru hoga kyuki yeh reasoning agent hai"
ACT = "act"
LAST = -1
def should_continue(state:MessagesState)->str:
    if not state["messages"][LAST].tools_calls:
        return END
    return ACT

flow = StateGraph(MessagesState)
flow.add_node(AGENT_REASON,run_agent_reasoning)
flow.set_entry_point(AGENT_REASON)
flow.add_node(ACT,tools_node)
flow.add_conditional_edges(AGENT_REASON,should_continue, {
    END:END,
    ACT:ACT
})

flow.add_edge(ACT,AGENT_REASON)
app = flow.compile()
app.get_graph().draw_mermaid_png(output_file_path = "flow.png")

if __name__ == "__main__":
    print("hello")
    # print(os.getenv("INDEX_NAME"))