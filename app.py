from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

LANGFLOW_FLOW_LINK = "Add your Langflow flow link here"
LANGFLOW_API_TOKEN = "Add your Langflow API Token here"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')

    # API request data
    data = {
        "input_value": user_input
    }

    # API headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer AstraCS:oGQGgxToyrmIyuyEFHBpzrbw:100b6c8b7b639a8037f4f2dd437c1fff189109bca6083ecb09570fed614d3eaa'
    }

    # API URL
    api_url = 'https://api.langflow.astra.datastax.com/lf/5a57d46e-69b1-49e7-ba2e-4c3930103e77/api/v1/run/2024b1c6-879f-48ac-a2f0-75d4a18e72d1?stream=false'

    try:
        # Send POST request to the API
        response = requests.post(api_url, headers=headers, json=data)
        response_json = response.json()

        # Extract the output text from the response
        output_text = response_json['outputs'][0]['outputs'][0]['results']['message']['text']

        return jsonify({'answer': output_text})
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error processing your request.'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
