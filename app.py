import streamlit as st
from ocr import extract_ingredients
from advisor import advisor_bot
from supervisor import supervisor_bot
from chat import chat_with_bot

st.set_page_config(page_title="🍽️ Food Ingredient Analyzer", layout="wide")

st.title("🍽️ Food Ingredient Analyzer")

# Sidebar for user info
st.sidebar.header("User Info")
medical_history = st.sidebar.text_input("Enter any medical conditions (optional)")

# Image upload section
st.header("📸 Upload Food Package Image")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Perform OCR
    with st.spinner("Extracting ingredients..."):
        ingredients = extract_ingredients("temp_image.jpg")
    
    st.subheader("Extracted Ingredients")
    st.write(ingredients)

    # Get health analysis
    with st.spinner("Analyzing health impact..."):
        health_analysis = advisor_bot(ingredients, medical_history)
    
    st.subheader("Health Analysis")
    st.write(health_analysis)

    # Supervisor validation
    with st.spinner("Validating health analysis..."):
        validation = supervisor_bot(health_analysis)
    
    st.subheader("Supervisor Validation")
    st.write(validation)

# Chatbot section
st.header("💬 Ask About Ingredients")
user_query = st.text_input("Ask about any ingredient or nutrition info:")
if user_query:
    response = chat_with_bot(user_query)
    st.write(response)
