from flask import Flask, request, jsonify
from google.cloud import aiplatform

app = Flask(__name__)

# Initialize Vertex AI (Gemini)
aiplatform.init(project="<YOUR_PROJECT_ID>", location="us-central1")

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    input_text = data.get("input", "")

    # Call Gemini model
    model = aiplatform.TextGenerationModel.from_pretrained("gemini-1.0-pro")
    response = model.predict(input_text, temperature=0.2, max_output_tokens=100)

    return jsonify({"summary": response.text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
