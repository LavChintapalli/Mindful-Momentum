import streamlit as st
import os

st.title("Diagnostic Mode 🔍")

# Check 1: Is the Secret Key there?
if "GOOGLE_API_KEY" in st.secrets:
    st.success("✅ Secret Key found in Streamlit Vault!")
else:
    st.error("❌ Secret Key NOT found in Streamlit Vault. Check Settings > Secrets.")

# Check 2: What is the current folder looking like?
st.write("Files Streamlit can see:")
st.code(os.listdir())

# Check 3: Is Streamlit library installed?
import streamlit
st.write(f"Streamlit Version: {streamlit.__version__}")