import paho.mqtt.client as mqtt
import json
import time

BROKER = "mqtt.eclipseprojects.io"
INPUT_TOPIC = "iot/sensors/#"
OUTPUT_TOPIC = "iot/aggregated_data"

def on_connect(client, userdata, flags, rc):
    print("Gateway connected to MQTT broker.")
    client.subscribe(INPUT_TOPIC)

def on_message(client, userdata, msg):
    print(f"Message received from sensor: {msg.payload.decode()}")
    data = json.loads(msg.payload.decode())
    aggregated_data = {
        "sensor_id": data["sensor_id"],
        "temperature": data["temperature"],
        "humidity": data["humidity"],
        "timestamp": time.time()
    }
    client.publish(OUTPUT_TOPIC, json.dumps(aggregated_data))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, 1883, 60)
client.loop_forever()
