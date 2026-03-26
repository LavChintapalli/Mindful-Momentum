# Version 2.0 - Final Push
import streamlit as st
import google.generativeai as genai

# 1. Access the "Vault" (Streamlit Secrets)
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
try:
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception:
    # Fallback to the newest version if the stable one is ever retired
    model = genai.GenerativeModel('gemini-3-flash-preview')
else:
    st.error("🔑 API Key not found! Check your Streamlit Secrets.")
    st.stop()

# 2. The Website Interface
st.title("Mindful Momentum 🧘‍♂️")
st.subheader("Leadership Presence in 30 Seconds")

if st.button("Generate a Leadership Tip"):
    with st.spinner("Connecting to Gemini..."):
        try:
            # Your leadership prompt
            response = model.generate_content("""
            Give me one 30-second mindfulness tip for a busy leader. 
            Randomly choose ONE category: Physical Stretch, Sensory Reset, or Mental Focus.
            Format your response like this:
            Category: [Category Name]
            Tip: [Your brief tip here]
            """)
            
            st.success("Success!")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Something went wrong: {e}")

# Mindful Momentum - Version 1.2