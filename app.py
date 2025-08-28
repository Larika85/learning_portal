import streamlit as st
from utils import generate_learning_path

st.set_page_config(page_title="Learning Portal", page_icon="📚", layout="wide")

st.title("📚 AI-Powered Learning Path Generator")

# Sidebar for API Key
st.sidebar.header("Configuration")
google_api_key = st.sidebar.text_input("Google API Key", type="password")

st.info("""
Enter your learning goal and Google API key.  
Example goals:
- "I want to learn Python basics in 3 days"
- "I want to learn data science basics in 10 days"
""")

# User goal input
st.header("Enter Your Goal")
user_goal = st.text_input("Learning goal:", help="E.g. 'Learn Python basics in 3 days'")

# Button
if st.button("Generate Learning Path", type="primary"):
    if not google_api_key:
        st.error("Please enter your Google API key in the sidebar.")
    elif not user_goal:
        st.warning("Please enter your learning goal.")
    else:
        try:
            with st.spinner("Generating your learning path..."):
                result = generate_learning_path(google_api_key, user_goal)
            st.success("Learning path generated! 🎉")
            st.header("Your Learning Path")
            st.markdown(result)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
