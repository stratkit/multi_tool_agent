import os

# Handle secrets/environment variables for both local and Streamlit
try:
    import streamlit as st
    if st.secrets:
        os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = st.secrets["GOOGLE_GENAI_USE_VERTEXAI"]
except ImportError:
    pass

from agent import root_agent
import asyncio

# --- Streamlit UI ---
try:
    import streamlit as st
    st.set_page_config(page_title="Multi-Tool Agent", layout="centered")
    st.title("🤖 mullt.ai — Your Multi-Agent Assistant")

    query = st.text_input("Ask your question:")

    if query:
        async def run_agent_and_return_response():
            result = ""
            async for event in root_agent.run_async(input=query):
                if event.is_final:
                    result = str(event.output)
            return result

        with st.spinner("Thinking..."):
            response = asyncio.run(run_agent_and_return_response())
            st.success("Done!")
            st.write(response)
except:
    print("Streamlit UI skipped — running in a non-Streamlit environment.")
