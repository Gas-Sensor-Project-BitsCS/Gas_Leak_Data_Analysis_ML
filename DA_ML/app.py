from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load pre-trained model only once
model = joblib.load("new_model.pkl")


class SensorData(BaseModel):
    MQ2: float
    TEMP: float
    HUMIDITY: float


@app.post("/predict")
def predict(data: SensorData):

    input_data = pd.DataFrame([{
        "MQ2": data.MQ2,
        "TEMP": data.TEMP,
        "HUMIDITY": data.HUMIDITY
    }])

    prediction = model.predict(input_data)[0]

    probabilities = model.predict_proba(input_data)[0]

    return {
        "MQ2": data.MQ2,
        "TEMP": data.TEMP,
        "HUMIDITY": data.HUMIDITY,
        "prediction": prediction,
        "confidence": round(float(max(probabilities)) * 100, 2)
    }