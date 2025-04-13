import streamlit as st
import os

from agent import root_agent  # adjust path if needed

# Load secrets (you’ll set these in Streamlit Cloud)
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = st.secrets["GOOGLE_GENAI_USE_VERTEXAI"]

st.set_page_config(page_title="Multi-Tool Agent", layout="centered")
st.title("🤖 mullt.ai — Your Multi-Agent Assistant")

import asyncio

query = st.text_input("Ask your question:")

if query:
    with st.spinner("Thinking..."):
        response = asyncio.run(root_agent.run_async(query))
        st.success("Done!")
        st.write(response)
