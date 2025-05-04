import google.generativeai as genai
import streamlit as st
from pygments.lexers import guess_lexer
from pygments.util import ClassNotFound
from pylint.lint import Run as lint

# Configure Gemini API for natural language explanations
genai.configure(api_key="AIzaSyCm3qaVkadN1jYvU13oEOOKMe-UkaAx13Q")  
model = genai.GenerativeModel('models/gemini-2.0-flash')

# Define the context for code explanation
code_context = """
You are an assistant designed to develop a creative story. Please:
1. Detect the content and emotions.
2. Prepare the lines for the story.
3. Identify and correct errors in the content if any.
4. Present the story by using simple english words.
"""

def initialize_session_state():
    if 'chat' not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])
        st.session_state.chat.send_message(code_context)
    if 'messages' not in st.session_state:
        st.session_state.messages = []

def detect_language(code):
    try:
        lexer = guess_lexer(code)
        return lexer.name
    except ClassNotFound:
        return "Unknown or unsupported language"

def main():
    st.title("Story Writing ✍️")
    st.markdown(
        """
        Put down your thoughts here and let the magic happen ✨*
        """
    )

    # Initialize session state
    initialize_session_state()

    # Code input
    code = st.text_area("Present your ideas here:")
    
    # Add Analyze button
    if st.button("Analyze Content"):
        if code:
            # Add user input to session state
            st.session_state.messages.append({"role": "user", "content": code})
            # with st.chat_message("user"):
            #     st.markdown(f"\n{code}\n")

            # Process the code: explain and correct
            with st.chat_message("assistant"):
                with st.spinner("Analyzing content..."):
                    response = st.session_state.chat.send_message(code)
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
        else:
            st.warning("Please enter some thoughts to analyze.")

if __name__ == "__main__":
    main()