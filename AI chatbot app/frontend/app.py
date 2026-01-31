import streamlit as st
import requests

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")
st.caption("Powered by Google Gemini | FastAPI + Streamlit")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        res = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"message": prompt},
            timeout=30
        )
        reply = res.json()["response"]
    except Exception:
        reply = "Unable to connect to backend."

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
