import random
import time
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io", 1883, 60)

def simulate_sensor_data():
    while True:
        temperature = random.uniform(20, 30)
        humidity = random.uniform(30, 50)
        payload = json.dumps({"temperature": temperature, "humidity": humidity})  # Перетворення в JSON
        print(f"Dispatch: {payload}")
        client.publish("iot/sensor_data", payload)
        time.sleep(2)

if __name__ == "__main__":
    simulate_sensor_data()
