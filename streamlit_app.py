import os
import asyncio

# Load environment variables from Streamlit secrets if available
try:
    import streamlit as st
    if st.secrets:
        os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = st.secrets["GOOGLE_GENAI_USE_VERTEXAI"]
except ImportError:
    # Not running in Streamlit, fallback to local env vars or .env file if used
    pass

from agent import root_agent

# --- Streamlit App ---
try:
    import streamlit as st

    st.set_page_config(page_title="Multi-Tool Agent", layout="centered")
    st.title("🤖 mullt.ai — Your Multi-Agent Assistant")

    query = st.text_input("Ask your question:")

    # Async wrapper for agent call
    async def run_agent_and_return_response():
        result = ""
        events = []

        st.write("⚙️ Starting agent...")

        try:
            async for event in root_agent.run_async(input=query):
                st.write("🔄 Event received")
                events.append(str(event))
                if event.is_final:
                    st.write("✅ Final response received")
                    result = str(event.output)
        except Exception as e:
            st.error(f"❌ Agent execution failed: {e}")
            return "Error during agent execution."

        # Show debug info
        st.subheader("Debug: Raw Agent Events")
        for e in events:
            st.text(e)

        return result

    if query:
        with st.spinner("Thinking..."):
            response = asyncio.run(run_agent_and_return_response())
            st.success("Done!")
            st.write("### 🧠 Response")
            st.write(response)

except Exception as e:
    print("Streamlit UI skipped — running in a non-Streamlit environment.")
    print(f"Exception: {e}")
