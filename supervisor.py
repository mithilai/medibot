from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API Key from .env
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# Initialize Supervisor LLM
supervisor_llm = ChatGroq(model_name="deepseek-r1-distill-llama-70b")

supervisor_prompt = PromptTemplate(
    input_variables=["advisor_response"],
    template="""
    You are a supervisor bot ensuring health advice accuracy.
    Review the following advisor response and verify its correctness:
    {advisor_response}
    """
)

def supervisor_bot(advisor_response):
    """Validates advisor's health assessment."""
    message = HumanMessage(content=supervisor_prompt.format(advisor_response=advisor_response))
    response = supervisor_llm.invoke([message])
    return response.content
