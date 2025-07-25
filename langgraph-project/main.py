from dotenv import load_dotenv
import os
load_dotenv()
from langchain_core.messages import BaseMessage, HumanMessage
from typing import List, Sequence
from langgraph.graph import END, MessageGraph
from chains import generation_chain, reflect_chain


REFLECT = "reflect"
GENERATE = "generate"

def generation_node(state: Sequence[BaseMessage]):
    return generation_chain.invoke({"messages": state})


def reflection_node(messages: Sequence[BaseMessage]) -> List[BaseMessage]:
    res = reflect_chain.invoke({"messages": messages})
    return [HumanMessage(content=res.content)]

def should_continue(state: List[BaseMessage]):
    if len(state)>6:
        return END
    return REFLECT
builder = MessageGraph()
builder.add_node(GENERATE,generation_node)
builder.add_node(REFLECT,reflection_node)
builder.set_entry_point(GENERATE)
builder.add_conditional_edges(GENERATE,should_continue, {END:END,REFLECT:REFLECT})
builder.add_edge(REFLECT,GENERATE)
graph = builder.compile()



if __name__ == "__main__":
    print("HELLO")
    inputs = HumanMessage(content="""Make this tweet better :
                    - BGMI is very good game and i enjoy thst playing very much
                    - I usually play with my friends i.e. Namdev and kc  

""")
    response = graph.invoke(inputs)
    print(response[-1].content)