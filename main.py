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

# Define the style separately to avoid formatting errors
brand_css = """
    <style>
    .stButton>button {
        background-color: #1d6788;
        color: white;
        border-radius: 5px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #154e68;
        color: white;
    }
    </style>
"""

# Now pass that variable to Streamlit
st.markdown(brand_css, unsafe_allow_html=True)

st.title("Mindful Momentum 🧘‍♂️")
st.write("*Micro-mindfulness for busy leaders.*")

st.divider()

# 3. The Menu
st.markdown("#### What kind of reset do you need?")

# Maintaining your preferred breathing room
st.markdown("<br>", unsafe_allow_html=True)

category = st.selectbox(
    "Label is hidden", # This stays in the background for screen readers
    options=["Mental Focus", "Physical Stretch", "Sensory Reset"],
    index=None,        # This makes the box start empty
    placeholder="Choose an option...", # This is the clean "Hint" inside the box
    label_visibility="collapsed"      # This hides the redundant "Label is hidden" text
)

# 4. The AI Logic
button_label = "Generate a Tip"

if st.button(button_label):
    if not category:
        st.warning("Please choose a reset type first! 👆")
    else:
        with st.spinner(f"Creating your {category} moment..."):
            try:
                prompt = f"Give me one 30-second {category} mindfulness tip for a busy leader. Be concise, actionable, and sophisticated."
                response = model.generate_content(prompt)
                
                # Your Beautiful Card UI
                st.markdown(f"""
                    <div style="
                        background-color: white; 
                        padding: 30px; 
                        border-radius: 15px; 
                        border: 1px solid #e0e0e0; 
                        border-top: 8px solid #1d6788; 
                        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                        margin: 20px 0;
                    ">
                        <h3 style="color: #1d6788; margin-top: 0; font-family: sans-serif;">✨ Your {category} Moment</h3>
                        <hr style="border: 0; border-top: 1px solid #eee; margin: 15px 0;">
                        <p style="color: #333; font-size: 1.15rem; line-height: 1.6; font-family: serif;">
                            {response.text}
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

            except Exception as e:
                # This is the "Graceful Fail" magic
                if "429" in str(e):
                    st.info("🧘‍♂️ **High Demand for Mindfulness!** Many leaders are using this tool right now. Please take a deep breath and try again in 60 seconds.")
                else:
                    # For any other weird error, we still show a clean message
                    st.error("Our AI coach is taking a quick break. Please refresh the page and try again!")

st.divider()
st.caption("Developed by Lav Chintapalli | Powered by Gemini AI")