import paho.mqtt.client as mqtt
import json
import requests

BROKER = "mqtt.eclipseprojects.io"
INPUT_TOPIC = "iot/sensors/#"
CLOUD_ENDPOINT = "http://cloud_connector:5000/data"

def on_connect(client, userdata, flags, rc):
    print("Gateway connected to MQTT broker.")
    client.subscribe(INPUT_TOPIC)

def on_message(client, userdata, msg):
    print(f"Message received from sensor: {msg.payload.decode()}")
    try:
        data = json.loads(msg.payload.decode())
        response = requests.post(CLOUD_ENDPOINT, json=data)
        print(f"Data sent to cloud, response: {response.status_code}")
    except Exception as e:
        print(f"Failed to send data: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.loop_forever()
