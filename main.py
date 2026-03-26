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
# This adds a custom CSS block to change the button color to your brand blue
st.markdown(f"""
    <style>
    .stButton>button {{
        background-color: #1d6788;
        color: white;
        border-radius: 5px;
        border: none;
    }}
    .stButton>button:hover {{
        background-color: #154e68;
        color: white;
    }}
    </style>
    """, unsafe_content_label=True)

st.title("Mindful Momentum 🧘‍♂️")
st.subheader("Micro-mindfulness for busy leaders.")

# 3. The Menu
category = st.selectbox(
    "What kind of reset do you need?",
    ["Mental Focus", "Physical Stretch", "Sensory Reset"]
)

# 4. The AI Logic
if st.button(f"Generate a {category} Tip"):
    with st.spinner(f"Creating your {category} moment..."):
        try:
            # We "inject" the category into the prompt so the AI knows what to do
            prompt = f"Give me one 30-second {category} mindfulness tip for a busy leader. Be concise, actionable, and sophisticated."
            response = model.generate_content(prompt)
            st.success(f"**Your {category} Tip:**")
            st.write(response.text)
        except Exception as e:
            st.error(f"AI Error: {e}")

st.divider()
st.caption("Developed by Lav Chintapalli | Powered by Gemini AI")