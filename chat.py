from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API Key from .env
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# Initialize Chatbot LLM
chat_llm = ChatGroq(model_name="llama-3.2-70b")

def chat_with_bot(query):
    """Allows users to ask about ingredients or nutrition info."""
    message = HumanMessage(content=query)
    response = chat_llm.invoke([message])
    return response.content
