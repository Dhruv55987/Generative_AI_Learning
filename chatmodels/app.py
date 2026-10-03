import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

st.set_page_config(page_title="Moodline", page_icon="🌊", layout="centered")

MODES = {
    "Angry 🔥": {
        "prompt": "You are an angry ai agent and reply very aggressively",
        "color": "#0F0503",
        "soft": "#F5E4DE",
    },
    "Sad 🌧️": {
        "prompt": "You are a sad ai agent and reply very depressed",
        "color": "#0D0A10",
        "soft": "#EAE4F2",
    },
    "Funny ✨": {
        "prompt": "You are a very funny ai agent and respond with humor and jokes",
        "color": "#0A0603",
        "soft": "#F3E7DC",
    },
}

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fraunces:wght@500&family=Inter:wght@400;500&display=swap');

    .stApp {
        background: linear-gradient(135deg, #EAF2EF 0%, #DCEAE5 100%);
    }
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    h1 {
        font-family: 'Fraunces', serif !important;
        font-weight: 500 !important;
        color: #223330 !important;
    }
    [data-testid="stChatMessage"] {
        border-radius: 16px;
        padding: 4px 6px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌊 Moodline")
st.caption("A little chatbot that matches whatever mood you pick.")

mode = st.selectbox("Choose a mode", list(MODES.keys()))
accent = MODES[mode]["color"]
soft = MODES[mode]["soft"]

st.markdown(f"""
    <style>
    [data-testid="stChatInput"] textarea {{
        border: 1.5px solid {accent}55 !important;
    }}
    div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarAssistant"]) {{
        background-color: {soft};
    }}
    </style>
""", unsafe_allow_html=True)

# Reset chat history whenever the mode changes
if "mode" not in st.session_state or st.session_state.mode != mode:
    st.session_state.mode = mode
    st.session_state.messages = [SystemMessage(content=MODES[mode]["prompt"])]

@st.cache_resource
def load_model():
    return init_chat_model("openai/gpt-oss-120b", model_provider="groq")

model = load_model()

# Show past messages (skip the system message)
for msg in st.session_state.messages[1:]:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)

user_input = st.chat_input("Say something…")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("thinking…"):
            response = model.invoke(st.session_state.messages)
        st.write(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))