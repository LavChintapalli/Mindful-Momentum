import streamlit as st
import google.generativeai as genai

# THE X-RAY TEST
st.write("--- DEBUGGING MODE ---")
if len(st.secrets) == 0:
    st.error("🕵️‍♂️ The Vault is COMPLETELY EMPTY. Streamlit can't see any secrets.")
else:
    st.success(f"🕵️‍♂️ Found {len(st.secrets)} secret(s) in the Vault.")
    st.write("Labels found:", list(st.secrets.keys()))

# Check for the specific key
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    st.success("✅ GOOGLE_API_KEY is linked and ready!")
else:
    st.error("❌ GOOGLE_API_KEY label not found. Check for typos in the Secrets box.")
    st.stop()