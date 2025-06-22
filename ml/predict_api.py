from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import mlflow.sklearn

app = FastAPI()

# Chemin exact vers le modèle MLflow
model = mlflow.sklearn.load_model("model")


# Structure des données d'entrée
class Passenger(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked_Q: int
    Embarked_S: int

@app.get("/")
def home():
    return {"message": "API Titanic prête 🚢"}

@app.post("/predict")
def predict(passenger: Passenger):
    data = pd.DataFrame([passenger.dict()])
    prediction = model.predict(data)[0]
    return {"prediction": int(prediction)}
