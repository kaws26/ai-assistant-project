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

# Add custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .chat-message.user {
        background-color: #2b313e;
    }
    .chat-message.assistant {
        background-color: #475063;
    }
    .chat-message .content {
        display: flex;
        flex-direction: row;
        align-items: flex-start;
    }
    .chat-message .avatar {
        width: 2rem;
        height: 2rem;
        margin-right: 1rem;
    }
    .chat-message .message {
        flex: 1;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

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
                json={"query": prompt, "user_id": os.getenv("USER_ID", "default_user")},
                headers={"X-User-ID": os.getenv("USER_ID", "default_user")}
            )
            response.raise_for_status()
            data = response.json()
            
            # Add AI responses to chat history
            st.session_state.messages.append({"role": "assistant", "content": data["casual_response"]})
            with st.chat_message("assistant"):
                st.write(data["casual_response"])
                
            st.session_state.messages.append({"role": "assistant", "content": data["formal_response"]})
            with st.chat_message("assistant"):
                st.write(data["formal_response"])
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()