from flask import Flask, render_template, request, jsonify
from model import get_gemini_response

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the user input from the request
        user_input = request.json.get('message', '').strip()

        if not user_input:
            return jsonify({'response': '❌ Error: No message received'}), 400

        # Call the model to get the response
        answer = get_gemini_response(user_input)

        if not answer:
            return jsonify({'response': '❌ Error: No response from model.'}), 500

        # Format the answer to return to the frontend with bold sections
        formatted_answer = format_response(answer)

        return jsonify({'response': formatted_answer})

    except Exception as e:
        print("Error during chat:", e)
        return jsonify({'response': '❌ Error: Unable to get response from Gemini.'}), 500


def format_response(answer):
    """
    Formats the chatbot's answer by removing unnecessary asterisks (*) and applying basic HTML formatting.
    """
    # Remove unnecessary asterisks (*) used for bold or bullet points
    cleaned_answer = answer.replace("*", "")

    # Optional: bold key phrases (can be expanded as needed)
    cleaned_answer = cleaned_answer.replace("Error", "<strong>Error</strong>")
    cleaned_answer = cleaned_answer.replace("No response", "<strong>No response</strong>")
    cleaned_answer = cleaned_answer.replace("response", "<strong>response</strong>")

    # Format the response into styled HTML
    formatted_answer = f"""
    <div class='response'>
        <h3>Response:</h3>
        <p>{cleaned_answer.replace('\n', '<br>')}</p>
    </div>
    """
    return formatted_answer


if __name__ == '__main__':
    app.run(debug=True)
