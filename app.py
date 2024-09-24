from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask application!"})

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "id": 1,
        "name": "Sample Data",
        "description": "This is a sample Flask API response."
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
