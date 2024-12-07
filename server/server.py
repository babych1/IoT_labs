
import paho.mqtt.client as mqtt
import json
import sqlite3
import time


conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sensor_data (timestamp REAL, sensor_id TEXT, temperature REAL, humidity REAL)''')
conn.commit()

def on_connect(client, userdata, flags, rc):
    print("Server connected to MQTT broker.")
    client.subscribe("iot/aggregated_data")

def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()}")
    data = json.loads(msg.payload.decode())
   
    c.execute("INSERT INTO sensor_data (timestamp, sensor_id, temperature, humidity) VALUES (?, ?, ?, ?)",
              (data["timestamp"], data["sensor_id"], data["temperature"], data["humidity"]))
    conn.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)
client.loop_forever()
