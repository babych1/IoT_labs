import random
import time
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io", 1883, 60)

def simulate_sensor_data():
    while True:
        meter_data = []
        for meter_id in range(1, 11):  
            consumption = random.uniform(0, 10)  
            meter_data.append({
                "meter_id": f"meter{meter_id}",
                "consumption": consumption
            })
        
        
        for data in meter_data:
            payload = json.dumps(data)
            print(f"Dispatch: {payload}")
            client.publish(f"iot/meters/{data['meter_id']}", payload)
            with open("meter_data.log", "a") as log_file:
                log_file.write(payload + "\n")
        
        time.sleep(random.uniform(1, 5))

if __name__ == "__main__":
    simulate_sensor_data()
