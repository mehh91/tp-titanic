from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import mlflow.sklearn

app = FastAPI()

# Chargement du modèle depuis le dossier 'model' enregistré avec MLflow
model = mlflow.sklearn.load_model("model")

# Définition du schéma d'entrée attendu pour une prédiction
class Passenger(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    SibSp: int
    Parch: int
    Fare: float
    Embarked_Q: int
    Embarked_S: int

# Endpoint de test (page d'accueil)
@app.get("/")
def home():
    return {"message": "API Titanic prête"}

# ✅ Nouveau endpoint pour vérifier l'état de l'API
@app.get("/health")
def health_check():
    return {"status": "ok", "model_loaded": True}

# Endpoint de prédiction
@app.post("/predict")
def predict(passenger: Passenger):
    data = pd.DataFrame([passenger.dict()])
    prediction = model.predict(data)[0]
    return {"prediction": int(prediction)}
