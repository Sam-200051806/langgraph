from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_groq import ChatGroq


reflection_prompt = ChatPromptTemplate(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. Generate critique and recommendations for the user's tweet."
            "Always provide detailed recommendations, including requests for length, virality, style, etc. ",
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

generation_prompt = ChatPromptTemplate(
    [
        (
            "system",
            "you are a twitter techie influencer assistant tasked with writing excellent twitter posts ."
            "Generate the best twitter post possible for the user's request."
            "If the user provides ceitique, respond with a revised version of your previous attempts.",
        ),
        MessagesPlaceholder(variable_name="messages")
    ]
)

llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0
)

generation_chain = generation_prompt | llm
reflect_chain = reflection_prompt | llm
