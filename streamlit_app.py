import os
import asyncio
import streamlit as st  # ✅ Only ONE import now

# Load environment variables from Streamlit secrets if available
try:
    if st.secrets:
        os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
        os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = st.secrets["GOOGLE_GENAI_USE_VERTEXAI"]
except ImportError:
    pass

from agent import root_agent
from google.adk.models import InvocationContext  # ✅ Add this line

st.set_page_config(page_title="Multi-Tool Agent", layout="centered")
st.title("🤖 mullt.ai — Your Multi-Agent Assistant")

query = st.text_input("Ask your question:")

# Async wrapper
async def run_agent_and_return_response():
    result = ""
    events = []

    st.write("⚙️ Starting agent...")

    try:
        # ✅ No context, just a string input
        async for event in root_agent.run_async(query):
            st.write("🔄 Event received")
            events.append(str(event))
            if event.is_final:
                st.write("✅ Final response received")
                result = str(event.output)
    except Exception as e:
        st.error("❌ Agent execution failed.")
        st.code(f"{type(e).__name__}: {e}")
        return "Error during agent execution."

    st.subheader("🛠️ Debug: Raw Agent Events")
    for e in events:
        st.text(e)

    return result

if query:
    with st.spinner("Thinking..."):
        response = asyncio.run(run_agent_and_return_response())
        st.success("Done!")
        st.write("### 🧠 Agent Response")
        st.write(response)
