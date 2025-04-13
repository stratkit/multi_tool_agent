import streamlit as st
import os
import asyncio
from agent import root_agent  # adjust as needed

# Load secrets (in Streamlit Cloud)
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = st.secrets["GOOGLE_GENAI_USE_VERTEXAI"]

st.set_page_config(page_title="Multi-Tool Agent", layout="centered")
st.title("🤖 mullt.ai — Your Multi-Agent Assistant")

query = st.text_input("Ask your question:")

async def run_agent(query):
    return await root_agent.run_async(query)

if query:
    with st.spinner("Thinking..."):
        response = asyncio.run(run_agent(query))
        st.success("Done!")
        st.write(response)
