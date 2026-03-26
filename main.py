import streamlit as st
import google.generativeai as genai

# 1. Access the "Vault" and Auto-Select Model
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    
    try:
        # This line asks Google: "What models do you have available for me?"
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        # This picks the very first working model from that list
        model = genai.GenerativeModel(models[0])
    except Exception as e:
        st.error(f"Connection Error: {e}")
        st.stop()
else:
    st.error("🔑 API Key not found in Streamlit Secrets!")
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