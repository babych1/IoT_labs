import paho.mqtt.client as mqtt
import json
import sqlite3
import datetime

conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS sensor_data (timestamp TEXT, temperature REAL, humidity REAL)''')
conn.close()

def on_connect(client, userdata, flags, rc):
    print("MQTT is connected with code " + str(rc))

    client.subscribe("iot/sensor_data")

def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()}")
    try:
        data = json.loads(msg.payload.decode())
        conn = sqlite3.connect('sensor_data.db')
        c = conn.cursor()
        c.execute("INSERT INTO sensor_data (timestamp, temperature, humidity) VALUES (?, ?, ?)", (str(datetime.datetime.now()), data["temperature"], data["humidity"]))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Data processing error: {e}")


client = mqtt.Client()


client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

if __name__ == "__main__":
    client.loop_forever()