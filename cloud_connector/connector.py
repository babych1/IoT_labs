from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)
app.debug = True

conn = sqlite3.connect('cloud_data.db', check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sensor_data (
    sensor_id TEXT,
    temperature REAL,
    humidity REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)''')
conn.commit()

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    c.execute("INSERT INTO sensor_data (sensor_id, temperature, humidity) VALUES (?, ?, ?)", 
              (data['sensor_id'], data['temperature'], data['humidity']))
    conn.commit()
    return jsonify({"status": "success"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    time_range = request.args.get('range', 'all') 
    conn = sqlite3.connect('cloud_data.db') 
    c = conn.cursor()

   
    if time_range == '1h':
        time_limit = str(datetime.now() - timedelta(hours=1))
        query = "SELECT timestamp, temperature, humidity FROM sensor_data WHERE timestamp >= ?"
        c.execute(query, (time_limit,))
    elif time_range == '24h':
        time_limit = str(datetime.now() - timedelta(days=1))
        query = "SELECT timestamp, temperature, humidity FROM sensor_data WHERE timestamp >= ?"
        c.execute(query, (time_limit,))
    elif time_range == '7d':
        time_limit = str(datetime.now() - timedelta(days=7))
        query = "SELECT timestamp, temperature, humidity FROM sensor_data WHERE timestamp >= ?"
        c.execute(query, (time_limit,))
    else:
        query = "SELECT timestamp, temperature, humidity FROM sensor_data"
        c.execute(query)

    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
