import random
import time
import requests

GATEWAY_URL = "http://gateway:5001/sensor_data"

def simulate_sensor_data():
    while True:
        temperature = random.uniform(20, 30)
        humidity = random.uniform(30, 50)
        payload = {"temperature": temperature, "humidity": humidity}
        print(f"Dispatch: {payload}")
        try:
            response = requests.post(GATEWAY_URL, json=payload)
            print(f"Gateway response: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(2)

if __name__ == "__main__":
    simulate_sensor_data()