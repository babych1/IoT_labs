from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Підключення до бази даних SQLite
conn = sqlite3.connect('iot_data.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sensor_data (temperature REAL, humidity REAL, timestamp TEXT)''')

def save_data(temperature, humidity):
    c.execute("INSERT INTO sensor_data (temperature, humidity, timestamp) VALUES (?, ?, datetime('now'))", (temperature, humidity))
    conn.commit()

@app.route('/sensor_data', methods=['POST'])
def receive_data():
    data = request.json
    print(f"Data received: {data}")
    save_data(data['temperature'], data['humidity'])
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)