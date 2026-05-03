import streamlit as st
from anthropic import Anthropic

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# ── System prompt presets ────────────────────────────────────────────────────
PRESETS = {
    "General Assistant": "You are a helpful, friendly AI assistant. Answer questions clearly and concisely.",
    "Tutor": (
        "You are a patient and encouraging tutor. Break down complex topics into simple steps. "
        "Use examples and analogies. Ask follow-up questions to check understanding."
    ),
    "Coding Assistant": (
        "You are an expert software engineer. Help with code reviews, debugging, architecture, "
        "and best practices. Always explain your reasoning and include code examples."
    ),
    "Friend": (
        "You are a warm, empathetic friend. Keep the tone casual and supportive. "
        "Listen actively, show genuine interest, and be encouraging."
    ),
    "Customer Support": (
        "You are a professional customer support agent. Be polite, patient, and solution-focused. "
        "Acknowledge issues, apologise when appropriate, and provide clear next steps."
    ),
}

# ── Session state initialisation ─────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "persona" not in st.session_state:
    st.session_state.persona = "General Assistant"

client = Anthropic()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("⚙️ Settings")

    selected = st.selectbox(
        "Choose Persona",
        list(PRESETS.keys()),
        index=list(PRESETS.keys()).index(st.session_state.persona),
    )
    if selected != st.session_state.persona:
        st.session_state.persona = selected
        st.session_state.messages = []
        st.rerun()

    st.markdown("**Current System Prompt:**")
    system_prompt = st.text_area(
        "System Prompt",
        value=PRESETS[st.session_state.persona],
        height=150,
        label_visibility="collapsed",
    )

    if st.button("🗑️ Reset Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.markdown(f"💬 **Messages:** {len(st.session_state.messages)}")

# ── Main UI ───────────────────────────────────────────────────────────────────
st.title("🤖 AI Chatbot")
st.caption(f"Persona: **{st.session_state.persona}**")

# Render chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if prompt := st.chat_input("Type your message…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                system=system_prompt,
                messages=st.session_state.messages,
            )
            reply = response.content[0].text

        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
