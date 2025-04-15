import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client using the secure secret
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit UI setup
st.set_page_config(page_title="MindMatch", page_icon="🎾")
st.title("🎾 MindMatch Sports Psychology Chatbot")
st.markdown(
    """
Welcome to **MindMatch**, your AI-powered mental training partner.
Write a journal entry about your tennis practice or match, and get personalized feedback to improve your mindset, focus, and recovery.
"""
)

# Journal input box
journal_input = st.text_area("📝 Your Journal Entry", height=200)

# Submit button logic
if st.button("Submit Entry"):
    if journal_input.strip() == "":
        st.warning("Please write a journal entry before submitting.")
    else:
        with st.spinner("Analyzing your entry and generating feedback..."):
            prompt = f"""
You are a compassionate, encouraging sports psychology chatbot named MindMatch.
The user is a college tennis player reflecting on a recent match or practice session.
Your job is to respond with short, evidence-based advice to improve their mental performance.

Their journal entry: {journal_input}

Respond with 3–4 sentences using a calm, positive tone.
Include one actionable suggestion like a mindfulness technique, breathing exercise, or focus cue.
Avoid medical advice or diagnosis.
"""

            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}]
                )
                feedback = response.choices[0].message.content
                st.success("✅ MindMatch Feedback:")
                st.write(feedback)
            except Exception as e:
                st.error(f"❌ Error from OpenAI: {e}")


