import os
import asyncio

# Load environment variables from Streamlit or local
try:
    import streamlit as st
    if st.secrets:
        os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = st.secrets["GOOGLE_GENAI_USE_VERTEXAI"]
except ImportError:
    pass

from agent import root_agent

# --- Streamlit UI ---
try:
    import streamlit as st
    st.set_page_config(page_title="Multi-Tool Agent", layout="centered")
    st.title("🤖 mullt.ai — Your Multi-Agent Assistant")

    query = st.text_input("Ask your question:")

    # ✅ Moved here — defined even if query is empty
    async def run_agent_and_return_response():
        result = ""
        events = []
        async for event in root_agent.run_async(input=query):
            events.append(str(event))
            if event.is_final:
                result = str(event.output)

        # Debug output of all agent events
        st.subheader("Debug: Raw Agent Events")
        for e in events:
            st.text(e)

        return result

    if query:
        with st.spinner("Thinking..."):
            response = asyncio.run(run_agent_and_return_response())
            st.success("Done!")
            st.write(response)

except Exception as e:
    print("Streamlit UI skipped — running in a non-Streamlit environment.")
    print(e)
