import streamlit as st
import openai
import os
from datetime import datetime

# ✅ Startup log
st.write("✅ Streamlit loaded")

# ✅ Check for OpenAI key
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    st.error("❌ OpenAI API key is missing. Add it in Streamlit Cloud > Advanced Settings > Secrets.")
else:
    st.write("✅ OpenAI API key detected")
    openai.api_key = api_key

# App layout
st.set_page_config(page_title="MindMatch", page_icon="🎾")
st.title("🎾 MindMatch Sports Psychology Chatbot")
st.markdown(
    """
Welcome to **MindMatch**, your AI-powered mental training partner.  
Write a journal entry about your tennis practice or match, and receive feedback to improve your mindset, focus, and recovery.
"""
)

# Journal input
journal_input = st.text_area("📝 Your Journal Entry", height=200)
st.write("✅ Text area loaded")

# Submit logic
if journal_input and st.button("Submit Entry"):
    with st.spinner("Analyzing your entry..."):
        try:
            prompt = f"""
You are a compassionate, encouraging sports psychology chatbot named MindMatch.
The user is a college tennis player reflecting on a recent match or practice.
Respond with short, supportive, evidence-based advice (3–4 sentences), including one mindfulness or breathing technique.
Avoid medical claims.

Journal entry: {journal_input}
"""

            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )

            feedback = response["choices"][0]["message"]["content"]
            st.success("✅ MindMatch Feedback")
            st.write(feedback)

            # Save entry
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"""
-------------------------
📅 {timestamp}
📝 Journal Entry:
{journal_input}

💬 Feedback:
{feedback}
-------------------------
"""
            with open("journal_log.txt", "a") as f:
                f.write(log_entry)

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")

# Download journal history
if os.path.exists("journal_log.txt"):
    with open("journal_log.txt", "r") as f:
        log_content = f.read()
    st.download_button("📥 Download Your Journal History", log_content, file_name="MindMatch_Journal_Log.txt")

st.markdown("---")
st.caption("Created for SCMP 401 — MindMatch by [Your Name]")
