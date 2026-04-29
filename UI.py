import streamlit as st
from query_data import query_rag

st.set_page_config(page_title="RAG Chatbot", page_icon="📟",layout="wide")
#st.title("✨Local Rag to answer Accounting✨")
st.markdown(
    """
    <h1 style='text-align: center; white-space: nowrap;'>
        ✨Local Rag to answer Accounting✨
    </h1>
    """, 
    unsafe_allow_html=True
)
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask me anything about your documents..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Query the RAG system and get the response
    with st.spinner("Thinking..."):
        
        response = query_rag(prompt) 
        
    # Display assistant response in chat message container
    with st.chat_message("My guy"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "My guy", "content": response})