import streamlit as st
import google.generativeai as genai

# 1. Access the "Vault" (Streamlit Secrets)
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    
    # This "try" block must be indented inside the "if"
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
    except Exception:
        model = genai.GenerativeModel('gemini-2.0-pro-exp')
else:
    # This "else" must line up with the "if" at the very start
    st.error("🔑 API Key not found! Check your Streamlit Secrets.")
    st.stop()

# 2. Website Design
st.set_page_config(page_title="Mindful Momentum", page_icon="🧘‍♂️")
st.title("Mindful Momentum 🧘‍♂️")
st.write("Micro-mindfulness for busy leaders.")

# 3. The AI Logic
if st.button("Generate a 30-Second Leadership Tip"):
    with st.spinner("Consulting the AI..."):
        try:
            prompt = "Give me one 30-second mindfulness tip for a busy leader. Be concise and actionable."
            response = model.generate_content(prompt)
            st.success("Here is your tip:")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI Error: {e}")

st.divider()
st.caption("Developed by Lav Chintapalli | Powered by Gemini AI")