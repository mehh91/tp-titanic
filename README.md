# Titanic MLOps – Déploiement complet sur AWS avec Terraform, Ansible et MLflow

## Objectif pédagogique

Ce projet met en œuvre un pipeline MLOps complet pour entraîner et déployer un modèle de prédiction de survie sur le Titanic, en automatisant :

- L’infrastructure cloud avec Terraform
- La configuration système avec Ansible
- Le suivi et la version des expériences avec MLflow
- Le packaging et le déploiement de l’API avec Docker

## Objectifs d'apprentissage

- Créer une infrastructure reproductible sur le cloud (AWS)
- Automatiser le déploiement de machines virtuelles avec Terraform
- Configurer automatiquement les serveurs avec Ansible
- Entraîner un modèle ML avec scikit-learn et le versionner avec MLflow
- Servir un modèle via une API REST

<pre> titanic-mlops/ ├── infra/ # Infrastructure AWS avec Terraform │ ├── main.tf │ ├── variables.tf │ ├── outputs.tf │ ├── provider.tf │ ├── terraform.tfvars # (à créer) │ └── mlops-key.pem # Clé SSH pour connexion ├── ansible/ # Configuration système avec Ansible │ ├── inventories/ │ │ └── hosts │ └── site.yml ├── ml/ # Code machine learning │ ├── train_model.py # Script d'entraînement MLflow │ ├── data_preprocessing.py# Nettoyage et transformation des données │ └── predict_api.py # API de prédiction FastAPI ├── model/ # Modèle entraîné et exporté ├── mlruns/ # Répertoire MLflow pour les expériences ├── requirements.txt # Dépendances Python └── README.md </pre>

## Prérequis techniques

- Compte AWS avec permissions EC2
- Terraform installé localement
- Ansible installé (ou Docker avec Ansible préconfiguré)
- Docker installé (optionnel pour MLflow local)
- Une clé SSH AWS (ex : mlops-key.pem) générée et associée à l'utilisateur

## Étape 1 : Ajouter vos credentials AWS

Créer le fichier infra/terraform.tfvars :

```hcl
aws_access_key    = "VOTRE_AWS_ACCESS_KEY"
aws_secret_key    = "VOTRE_AWS_SECRET_KEY"
aws_region        = "eu-west-3"

key_name          = "mlops-key"
private_key_path  = "./mlops-key.pem"
instance_name     = "titanic-mlops-instance"
instance_type     = "t2.micro"
ami_id            = "ami-04e601abe3e1a910f"
```

Déposez ensuite le fichier .pem correspondant dans infra/.

## Étape 2 : Déploiement de l'infrastructure avec Terraform

```bash
cd infra/
terraform init
terraform apply
```

Notez bien les IPs retournées (training_instance_ip, api_instance_ip).

## Étape 3 : Configuration automatique avec Ansible

```bash
cd ..
ansible-playbook -i ansible/inventories/hosts ansible/site.yml
```

Ce playbook :
- Installe Python3, pip, virtualenv
- Crée l’environnement Python
- Installe les packages pour l’entraînement et l’API

## Étape 4 : Entraînement du modèle sur la machine training

```bash
ssh -i infra/mlops-key.pem ubuntu@<training_instance_ip>
cd titanic-mlops
source venv/bin/activate
python ml/train_model.py
```

Le modèle est enregistré automatiquement dans MLflow Registry.

## Étape 5 : Accès à MLflow UI (optionnel)

```bash
mlflow ui --host 0.0.0.0 --port 5000
```

Puis dans le navigateur :

```
http://<training_instance_ip>:5000
```

## Exemple d'appel API

### Endpoint : `/predict`

**Méthode** : POST  
**URL** : http://<api_instance_ip>:5000/predict

**Exemple de requête :**
```json
{
  "Pclass": 3,
  "Sex": "male",
  "Age": 22,
  "Fare": 7.25
}
```

**Réponse attendue :**
```json
{
  "prediction": 0
}
```

### Endpoint : `/health`

**Méthode** : GET  
**URL** : http://<api_instance_ip>:5000/health

**Réponse attendue :**
```json
{
  "status": "ok",
  "model_loaded": true
}
```

## Résultats attendus

- Modèle entraîné et tracké dans MLflow
- Suivi des expériences opérationnel
- Infrastructure reproductible sur AWS
- API en état de prédire avec le modèle sauvegardé

## Auteurs

Mehdi YAKOUBENE et Mehdi LOULIZI  
Projet MLOps – Juin 2025
