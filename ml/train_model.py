import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score

# Chargement des données prétraitées depuis les fichiers CSV
X = pd.read_csv("data/features.csv")  # Données d'entrée (features)
y = pd.read_csv("data/target.csv")    # Variable cible (target)

# Séparation des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialisation de l'expérience MLflow (nommée "titanic")
mlflow.set_experiment("titanic")

# Démarrage d'un enregistrement (run) MLflow
with mlflow.start_run():
    # Déclaration et entraînement du modèle de régression logistique
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)

    # Prédictions sur les données de test
    y_pred = model.predict(X_test)

    # Évaluation des performances avec deux métriques
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Enregistrement des métriques dans MLflow
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)

    # Sauvegarde du modèle entraîné dans MLflow (format scikit-learn)
    mlflow.sklearn.log_model(model, "model")

    # Message de confirmation
    print("✅ Modèle entraîné et enregistré dans MLflow")
