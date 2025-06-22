# Utilise une image Python officielle
FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port de l'API
EXPOSE 8000

# Lancer Uvicorn
CMD ["uvicorn", "ml.predict_api:app", "--host", "0.0.0.0", "--port", "8000"]
