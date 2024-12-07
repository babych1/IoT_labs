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
        if not (15 <= temperature <= 35):
            print(f"Warning: Temperature out of range: {temperature}")
            continue

        if not (20 <= humidity <= 60):
            print(f"Warning: Humidity out of range: {humidity}")
            continue
        payload = json.dumps({"sensor_id": "sensor1", "temperature": temperature, "humidity": humidity})
        print(f"Dispatch: {payload}")
        client.publish("iot/sensors/sensor1", payload)
        with open("sensor_data.log", "a") as log_file:
            log_file.write(payload + "\n")
        
        time.sleep(random.uniform(1, 5))

if __name__ == "__main__":
    simulate_sensor_data()