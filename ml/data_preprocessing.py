import pandas as pd

# Charger les données
df = pd.read_csv("data/train.csv")

# Nettoyage
df.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis=1, inplace=True)
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

# Séparer features / cible
X = df.drop("Survived", axis=1)
y = df["Survived"]

# Sauvegarder les fichiers pour l'entraînement
X.to_csv("data/features.csv", index=False)
y.to_csv("data/target.csv", index=False)

print("✅ Données préparées")
