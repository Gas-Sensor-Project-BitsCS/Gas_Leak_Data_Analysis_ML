import random
import time
import requests

API_URL = "http://127.0.0.1:8000/predict"


def generate_random_data():

    sensor_data = {
        "MQ2": round(random.uniform(0, 50), 2),
        "TEMP": round(random.uniform(15, 50), 2),
        "HUMIDITY": round(random.uniform(20, 90), 2)
    }

    return sensor_data


while True:

    # Generate random sensor data
    data = generate_random_data()

    try:

        # Send data to pre-trained ML model
        response = requests.post(
            API_URL,
            json=data,
            timeout=5
        )

        response.raise_for_status()

        result = response.json()

        print("\n==========================")
        print("NEW SENSOR DATA")
        print("==========================")

        print("MQ2:", data["MQ2"])
        print("TEMP:", data["TEMP"])
        print("HUMIDITY:", data["HUMIDITY"])

        print("\nMODEL PREDICTION")
        print("Status:", result["prediction"])
        print("Confidence:", result["confidence"], "%")

    except requests.RequestException as e:

        print("Error:", e)

    # Generate next reading after 2 seconds
    time.sleep(2)