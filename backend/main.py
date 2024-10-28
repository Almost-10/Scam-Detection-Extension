from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/check-conversation', methods=['POST'])
def check_conversation():
    data = request.get_json()
    conversation = data.get("conversation", "")
    # Add logic to process 'conversation' if needed
    return jsonify({"response": "Sample Response"}), 200

# Endpoint 2: /check-exif
@app.route('/check-exif', methods=['POST'])
def check_exif():
    data = request.get_json()
    exif = data.get("exif", "")
    claim = data.get("claim", "")
    # Add logic to process 'exif' and 'claim' if needed
    return jsonify({"response": "Sample Response"}), 200

if __name__ == "__main__":
    app.run(debug=True)