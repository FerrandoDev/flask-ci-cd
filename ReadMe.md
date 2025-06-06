# Projet Flask API + MySQL via Docker

Ce projet est une API REST développée avec **Flask (Python)** qui lit des articles depuis une base de données **MySQL** hébergée dans un conteneur **Docker**.

## Fonctionnalité

L'API expose un endpoint unique :

GET /articles

Ce endpoint retourne un JSON contenant une liste d’articles stockés en base de données.

---

## Structure du projet

flask-ci-cd/
├── app/
│ ├── init.py # Initialise l'application Flask
│ ├── routes.py # Définit les routes (endpoints)
├── config.py # Configuration de la base de données
├── run.py # Point d'entrée de l'application
├── docker-compose.yml # Lance MySQL dans Docker
├── mysql-init/
│ └── init.sql # Script SQL : création + insertion des articles

---

## Prérequis

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker + Docker Compose](https://www.docker.com/products/docker-desktop)
- [pip](https://pip.pypa.io/en/stable/installation/)

---

## Installation du projet

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/ton-utilisateur/ton-projet.git
   cd ton-projet
Lancer MySQL avec Docker
docker compose up -d

Créer un environnement virtuel Python
python -m venv venv
source venv/Scripts/activate  # (Windows)

Installer les dépendances
pip install flask mysql-connector-python

Lancer le serveur Flask
python run.py

Tester l'API
Ouvrir dans le navigateur ou Postman :
http://localhost:5000/articles

🛠️ Détails techniques

📦 Docker Compose
Le fichier docker-compose.yml installe automatiquement MySQL avec les paramètres suivants :

Host: localhost

Port: 3306

Base de données : flaskdb

Utilisateur : flaskuser

Mot de passe : flaskpass

Le script SQL mysql-init/init.sql :

Crée une table articles

Ajoute 5 articles de démonstration

Connexion à la BDD
La connexion se fait depuis routes.py avec mysql.connector :

conn = mysql.connector.connect(**DB_CONFIG)
cursor.execute("SELECT * FROM articles")
Les données sont renvoyées au format JSON avec jsonify().

 Exemple de réponse
[
  {
    "id": 1,
    "titre": "Article 1",
    "contenu": "Contenu de l'article 1",
    "dt_publication": "2025-06-06T00:00:00"
  }
]
🧪 Tests
(à venir) Tu pourras ajouter des tests unitaires avec pytest.

🧰 Auteur
Projet individuel réalisé par FERRANDO FABIEN dans le cadre de l’évaluation DevOps CI/CD - 3WA.

📅 Livraison
Rendu attendu sur GitHub en public avant le 11/04/2025 23h00.