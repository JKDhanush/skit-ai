import streamlit as st
from components.sidebar import render_sidebar
from utils.api import generate_response

st.set_page_config(page_title="RecoverAI Copilot", page_icon="🤖", layout="wide")

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 RecoverAI Copilot")
st.caption("AI-powered customer response generator")
st.markdown('*Example: "I\'m facing financial issues right now. Can I get more time to pay my bill?"*')

# Sidebar
settings = render_sidebar()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
user_input = st.chat_input("Type customer message...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Call backend
    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            try:
                response = generate_response(
                    user_input,
                    settings["tone"],
                    settings["length"]
                )
                bot_reply = response.get("response", "No response")
            except Exception as e:
                bot_reply = f"Error: {e}"

        st.write(bot_reply)

    # Save response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})