import streamlit as st
import chatbot_backend as demo  # Importing the chatbot functions from backend

# Set title of the chatbot interface
st.title("Hi, This is Chatbot Adedayo Ademuyiwa :sunglasses:")

# Initialize LangChain memory in session state if not already done
if 'memory' not in st.session_state:
    st.session_state.memory = demo.demo_memory()

# Initialize chat history in session state if not already done
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

# Capture user input via chat input box
input_text = st.chat_input("Powered by Bedrock and Claude")
if input_text:
    # Display the user message
    with st.chat_message("user"):
        st.markdown(input_text)

    # Append user message to chat history
    st.session_state.chat_history.append({"role": "user", "text": input_text})

    # Get the chatbot response
    chat_response = demo.demo_conversation(input_text=input_text, memory=st.session_state.memory)

    # Display the assistant's response
    with st.chat_message("assistant"):
        st.markdown(chat_response)

    # Append assistant's response to chat history
    st.session_state.chat_history.append({"role": "assistant", "text": chat_response})
