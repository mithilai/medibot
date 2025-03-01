from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import base64
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API Key from .env
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")


# Initialize OCR LLM
ocr_llm = ChatGroq(model_name="llama-3.2-90b-vision-preview")

def extract_ingredients(image_path):
    """Extract ingredients using LLaMA 3.2 Vision model."""
    with open(image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode("utf-8")
    
    prompt = "Extract the ingredients from the provided image."
    
    message = HumanMessage(
        content=[
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}},
            {"type": "text", "text": prompt},
        ]
    )

    response = ocr_llm.invoke([message])
    return response.content
