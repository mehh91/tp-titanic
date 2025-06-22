
#  Titanic MLOps – Déploiement complet sur AWS avec Terraform, Ansible et MLflow

Ce projet met en œuvre un pipeline MLOps complet pour entraîner un modèle de prédiction de survie sur le Titanic, en automatisant toute l’infrastructure avec **Terraform**, la configuration système avec **Ansible**, et le suivi d’expériences avec **MLflow**.

---

##  Objectifs pédagogiques

- Créer une infrastructure cloud avec **Terraform**
- Configurer les machines automatiquement avec **Ansible**
- Entraîner un modèle ML avec **scikit-learn** et **MLflow**
- Suivre et versionner les expériences de machine learning

---

##  Arborescence du projet

```bash
titanic-mlops/
├── infra/                     # Infrastructure AWS avec Terraform
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   ├── provider.tf
│   ├── terraform.tfvars       <-- À créer (voir plus bas)
│   └── mlops-key.pem          <-- À fournir (clé SSH AWS)
├── ansible/                   # Configuration avec Ansible
│   ├── inventories/
│   │   └── hosts
│   └── site.yml
├── ml/                        # Code Python ML
│   ├── train_model.py
│   ├── data_preprocessing.py
│   └── predict_api.py
├── model/                     # Modèle entraîné
├── mlruns/                    # Expériences MLflow
├── requirements.txt
└── README.md
```

---

##  Prérequis

- Un compte AWS avec droits EC2/IAM
- `Terraform` installé
- `Ansible` (ou utiliser le conteneur Docker fourni)
- `Docker` (optionnel pour MLflow local)
- Une paire de clés SSH créée sur AWS (`mlops-key.pem`)

---

## Étape 1 : Ajouter vos credentials AWS

Avant de lancer Terraform, dans le fichier suivant :

📄 `infra/terraform.tfvars`
```hcl
# Remplacez ces valeurs par VOS informations AWS

aws_access_key    = "VOTRE_AWS_ACCESS_KEY"
aws_secret_key    = "VOTRE_AWS_SECRET_KEY"
aws_region        = "eu-west-3"  # Région de Paris

key_name          = "mlops-key"               # Nom de la clé SSH créée sur AWS
private_key_path  = "./mlops-key.pem"         # Clé .pem dans le dossier infra
instance_name     = "titanic-mlops-instance"
instance_type     = "t2.micro"
ami_id            = "ami-04e601abe3e1a910f"    # Ubuntu 22.04 LTS (Paris)
```

Ajoutez également votre clé `.pem` téléchargée dans `infra/`.

---

## Étape 2 : Lancer l'infrastructure avec Terraform

```bash
cd infra/
terraform init
terraform apply
```

Notez les IPs générées par Terraform (`training_instance_ip`, `api_instance_ip`).

---

## Étape 3 : Lancer Ansible pour configurer les serveurs

```bash
cd ..
ansible-playbook -i ansible/inventories/hosts ansible/site.yml
```

Ansible va :
- Installer Python3, pip
- Créer un environnement virtuel
- Installer les dépendances
- Préparer le serveur pour l'entraînement et l’API

---

## Étape 4 : Entraîner le modèle

Connectez-vous au serveur d'entraînement (via l’IP donnée par Terraform) :

```bash
ssh -i infra/mlops-key.pem ubuntu@<training_instance_ip>
cd titanic-mlops
source venv/bin/activate
python ml/train_model.py
```

Le modèle est suivi et versionné dans MLflow.

---

## Étape 5 : Lancer MLflow UI (facultatif)

Sur le serveur :

```bash
mlflow ui --host 0.0.0.0 --port 5000
```

Puis ouvrir : http://<training_instance_ip>:5000

---

## Résultat attendu

- Modèle entraîné, enregistré dans `model/`
- Suivi d’expérience MLflow visible
- Infrastructure reproductible sur AWS
- Projet prêt pour déploiement de l’API (FastAPI ou Flask)


- Mehdi YAKOUBENE et Mehdi LOULIZI – Projet MLOps – Juin 2025
"# titanic-tp" 
