from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API Key from .env
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# Initialize Advisor LLM
advisor_llm = ChatGroq(model_name="llama-3.2-11b-vision-preview")

advisor_prompt = PromptTemplate(
    input_variables=["ingredients", "medical_history"],
    template="""
    You are a health advisor bot. The extracted ingredients are: {ingredients}.
    The user's medical history (if provided) is: {medical_history}.
    Analyze and provide a health assessment, highlighting any risks.
    """
)

def advisor_bot(ingredients, medical_history="None"):
    """Analyzes health risks based on extracted ingredients."""
    message = HumanMessage(content=advisor_prompt.format(ingredients=ingredients, medical_history=medical_history))
    response = advisor_llm.invoke([message])
    return response.content
