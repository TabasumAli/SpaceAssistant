# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

# Step1: Setup UI with Streamlit
import streamlit as st
import requests

st.set_page_config(page_title="Space Data AI Assistant", layout="centered")
st.title("🌌 Space Data AI Assistant")
st.write("Ask about space research, astronomy, and space exploration!")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query: ", height=150, placeholder="Ask anything about space!")

API_URL = "https://spaceassistant.onrender.com/chaat"

if st.button("Ask Agent!"):
    if user_query.strip():
        # Step2: Connect with backend via URL
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": "You are a Space Assistant, an AI expert in space research, astronomy, and space exploration. Your goal is to provide accurate, insightful, and engaging responses to questions about space, planets, missions, and the universe.",
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")
