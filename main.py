import os
import google.generativeai as genai
from dotenv import load_dotenv

# Step 1: Reach into the .env vault and grab the key
load_dotenv()
MY_KEY = os.getenv("GOOGLE_API_KEY")

try:
    # Step 2: Configure the AI
    genai.configure(api_key=MY_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Step 3: Send the request and show the result
    print("Connecting to Gemini...")
    
    response = model.generate_content("""
    Give me one 30-second mindfulness tip for a busy leader. 
    Randomly choose ONE category: Physical Stretch, Sensory Reset, or Mental Focus.
    Format your response like this:
    Category: [Category Name]
    Tip: [Your brief tip here]
    """)
    
    print("\n--- SUCCESS! ---")
    print(response.text)

except Exception as e:
    print(f"\n--- ERROR ---")
    print(f"Something went wrong: {e}")

    # Mindful Momentum - Version 1.0