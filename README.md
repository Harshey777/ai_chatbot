# 🤖 AI Chatbot (Custom Assistant)

A conversational AI chatbot built with Streamlit and the Anthropic Claude API. Switch between
personas, maintain full conversation history, and reset chats in one click.

---

## Features

- **Real-time chat interface** — clean chat bubbles, auto-scroll, spinner while generating
- **Conversation history** — full multi-turn context sent on every request
- **5 built-in personas** — General Assistant, Tutor, Coding Assistant, Friend, Customer Support
- **Editable system prompt** — customise the active persona directly in the sidebar
- **Reset chat** — clear history and start fresh without restarting the app

---

## Tech Stack

| Layer | Tool |
|-------|------|
| Frontend | Streamlit |
| AI Model | Anthropic Claude (claude-sonnet-4) |
| Language | Python 3.10+ |

---

## Project Structure

```
1_ai_chatbot/
├── app.py            # Main Streamlit application
├── requirements.txt  # Python dependencies
└── README.md
```

---

## Setup & Run

### 1. Clone / download this folder

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your Anthropic API key

**Option A – environment variable (recommended)**
```bash
export ANTHROPIC_API_KEY="sk-ant-..."   # Linux / macOS
set  ANTHROPIC_API_KEY=sk-ant-...       # Windows CMD
```

**Option B – Streamlit secrets**

Create `.streamlit/secrets.toml`:
```toml
ANTHROPIC_API_KEY = "sk-ant-..."
```

Then update `app.py` to read `st.secrets["ANTHROPIC_API_KEY"]` and pass it to the client.

### 5. Run the app
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## Usage

1. Select a **Persona** from the sidebar dropdown.
2. Optionally edit the **System Prompt** to further customise behaviour.
3. Type a message in the chat box and press **Enter**.
4. Click **Reset Chat** to clear the conversation.

---

## Customisation Tips

- Add more personas by extending the `PRESETS` dict in `app.py`.
- Swap `claude-sonnet-4-20250514` for another Claude model (e.g. `claude-haiku-4-5-20251001` for faster, cheaper responses).
- Increase `max_tokens` for longer replies.

---

## Use Cases

- Customer support bot
- Personal AI assistant
- Study / tutoring companion
- Coding helper
