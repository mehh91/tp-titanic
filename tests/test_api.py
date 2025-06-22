from fastapi.testclient import TestClient
from predict_api import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API Titanic prête 🚢"}

def test_predict_survives():
    sample_input = {
        "Pclass": 3,
        "Sex": 1,
        "Age": 22.0,
        "SibSp": 1,
        "Parch": 0,
        "Fare": 7.25,
        "Embarked_Q": 0,
        "Embarked_S": 1
    }
    response = client.post("/predict", json=sample_input)
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in [0, 1]
