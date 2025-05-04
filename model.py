import google.generativeai as genai

# Configure Gemini API key
API_KEY = "AIzaSyA3UJ24-RZ_xAGpC3xsZSr7aEcq8kg4AIU"
genai.configure(api_key=API_KEY)

# Initialize model and start a chat session (with memory)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
chat_session = model.start_chat(history=[])

def get_gemini_response(user_input):
    try:
        # Use chat_session to keep memory
        response = chat_session.send_message(user_input)
        return response.text.strip()
    except Exception as e:
        print("Error during model generation:", e)
        return None
