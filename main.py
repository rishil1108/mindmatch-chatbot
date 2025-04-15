from openai import OpenAI
import streamlit as st
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="MindMatch", page_icon="🎾")
st.title("🎾 MindMatch Sports Psychology Chatbot")
st.markdown("Write a journal entry about today’s practice or match below:")

journal_input = st.text_area("Your Journal Entry")

if st.button("Submit"):
    if journal_input.strip() == "":
        st.warning("Please write something before submitting.")
    else:
        with st.spinner("Analyzing your entry..."):
            prompt = f'''
You are a compassionate sports psychology chatbot named MindMatch. 
The user is a collegiate tennis player writing a journal after practice or a match.
They need psychological feedback to improve performance.

Journal entry: {journal_input}

Give calm, positive, evidence-based mental performance advice in 3–4 sentences.
Avoid medical claims. Offer simple techniques like breathing, mindfulness, or focus strategies.
            '''
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            advice = response.choices[0].message.content
            st.subheader("🧠 MindMatch Advice")
            st.write(advice)
