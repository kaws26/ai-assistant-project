import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Get backend URL from environment or use relative path
BACKEND_URL = os.getenv("BACKEND_URL", "")

def main():
    st.title("AI Assistant 🤖")
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Get AI response
        try:
            response = requests.post(
                f"{BACKEND_URL}/api/generate",
                json={"message": prompt},
                headers={"X-User-ID": os.getenv("USER_ID", "default_user")}
            )
            response.raise_for_status()
            ai_response = response.json()["response"]
            
            # Add AI response to chat history
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            with st.chat_message("assistant"):
                st.write(ai_response)
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()