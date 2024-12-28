# Import Necessary LangChain Modules

from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain_aws import ChatBedrock

# Function to Initialize the Chatbot Model

def demo_chatbot():
    #Initialize the FM with required paramters using ChatBedrock
    demo_llm = ChatBedrock(
        credentials_profile_name='default', # AWS profile name
        model_id='anthropic.claude-3-haiku-20240307-v1:0',
        model_kwargs={
            "max_tokens": 300,
            "temperature": 0.1,
            "top_p": 0.9,
            "stop_sequences": ["\n\nHuman:"]  
        }
    )
    return demo_llm

# Function to initialize memory for conversation

def demo_memory():
    # Initiliaze memory using the demo_chatbot function
    memory = ConversationSummaryBufferMemory(llm=demo_chatbot(), max_token_limit=300)
    return memory

# Function to manage conversation with the chatbot

def demo_conversation(input_text, memory):
    # Initialize the conversation chain with the chatbot model and memory
    llm_conversation = ConversationChain(llm=demo_chatbot(), memory=memory, verbose=True)
    # Get the response from the model

    chat_reply = llm_conversation.invoke(input_text)
    return chat_reply['response']
