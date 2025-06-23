from dotenv import load_dotenv
load_dotenv()
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch



@tool
def triple(num:float) -> float:
    """
    Just Triple the number
    """
    return float(num) * 3

tools = [TavilySearch(max_results = 1),triple]
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
).bind_tools(tools)