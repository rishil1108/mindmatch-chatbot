import streamlit as st
import openai
import os

# ✅ Step 1: Debug start
st.write("✅ Streamlit started")

# ✅ Step 2: Check API Key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("❌ OPENAI_API_KEY is missing in Streamlit secrets.")
    st.stop()

st.write("✅ API Key found")
openai.api_key = api_key

# ✅ Step 3: Title and input
st.title("🎾 MindMatch Chatbot")
st.markdown("Write a journal entry about your tennis practice or match:")

entry = st.text_area("📝 Journal Entry")

# ✅ Step 4: Submit and respond
if st.button("Submit") and entry.strip():
    with st.spinner("Analyzing your entry..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "user", "content": f"Give calm psychological advice based on this tennis journal entry: {entry}"}
                ]
            )
            st.write("✅ Chatbot response:")
            st.success(response["choices"][0]["message"]["content"])
        except Exception as e:
            st.error(f"❌ Error: {e}")
