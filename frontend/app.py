import streamlit as st
from helpers.faq import get_response
# Set up the Streamlit app
st.set_page_config(page_title="Automated Customer Assistance", layout="centered")

# Sidebar for selecting customer support options
st.sidebar.title("Customer Assistance")
options = st.sidebar.radio("How can we assist you?", ["Chatbot", "FAQ", "Contact Us"])

# Display different interfaces based on the selected option
if options == "Chatbot":
    st.title("Chat with our Assistant")
    
    # Chatbot conversation interface
    chat_history = st.empty()
    user_input = st.text_input("You: ", "")

    if user_input:
        # Get the chatbot's response (can be extended with NLP)
        response = get_response(user_input)
        st.write(f"Bot: {response}")

elif options == "FAQ":
    st.title("Frequently Asked Questions")
    st.write("Here are some of the common questions our customers ask:")
    st.write("""
    1. **What is your return policy?**
    2. **How long does shipping take?**
    3. **What payment methods are accepted?**
    4. **How do I track my order?**
    5. **How can I contact customer support?**
    """)

elif options == "Contact Us":
    st.title("Contact Us")
    st.write("For further assistance, please reach out to us via:")
    st.write("""
    - **Email:** support@company.com
    - **Phone:** +1 800 123 4567
    """)