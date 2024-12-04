from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
SERVER_URL = "http://server:5000/sensor_data"

@app.route('/sensor_data', methods=['POST'])
def receive_sensor_data():
    data = request.json
    print(f"Received data from the sensor: {data}")
    try:
        response = requests.post(SERVER_URL, json=data)
        print(f"Server response: {response.status_code}")
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)