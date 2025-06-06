# Projet CI/CD : API Flask + MySQL via Jenkins

## Contexte
Ce projet a pour objectif de développer une API REST en Python (Flask) qui lit des articles depuis une base de données MySQL, puis de mettre en place un pipeline CI/CD automatisé via Jenkins.

## Structure du dépôt
.
├── app/
│ ├── init.py # Création de l'app Flask
│ └── routes.py # Route /articles interrogeant MySQL
├── test/
│ └── test_articles.py # Test unitaire avec mock de la BDD
├── conftest.py # Fixture pytest pour FlaskClient
├── config.py # DB_CONFIG (host='db', user='flaskuser', …)
├── Dockerfile # (optionnel) Image Flask pour local/test
├── Dockerfile-jenkins # Image Jenkins avec Python et git
├── Jenkinsfile # Pipeline CI/CD simplifié
├── Makefile # Commandes make (docker-compose local, etc.)
├── requirements.txt # flask, mysql-connector-python, pytest
├── run.py # Point d'entrée Flask
└── README.md # Ce fichier

---

## Partie 1 : Développement de l’API Flask

#### 1. Créer un environnement Python :

   ```
   python -m venv venv
   source venv/bin/activate   # (Windows : .\venv\Scripts\activate)
   pip install --upgrade pip
   pip install -r requirements.txt
   ```
Lancer MySQL en local (si vous voulez tester la BDD) :

`docker-compose up -d db`

Initialiser la BDD (script init.sql dans mysql-init/).

Lancer le serveur Flask :

`python run.py`

Tester l’endpoint dans un navigateur ou Postman :
GET http://localhost:5000/articles doit renvoyer la liste JSON des articles.

# Partie 2 : Configuration de MySQL (local)

Service db dans docker-compose.yaml (à décommenter pour local : voir ancienne version)

init.sql initialise la base flaskdb, crée l’utilisateur flaskuser et insère 5 articles.

config.py contient :

````
DB_CONFIG = {
    "host": "db",
    "user": "flaskuser",
    "password": "flaskpass",
    "database": "flaskdb",
    "port": 3306
}
````

# Partie 3 : Tests Unitaires

Test test/test_articles.py utilise unittest.mock pour simuler la connexion à MySQL.

Commande en local :

`pytest`

# Partie 4 : Pipeline CI/CD avec Jenkins
Construire et démarrer Jenkins (depuis la racine du projet) :

docker-compose up -d jenkins
Récupérer le mot de passe initial :

`docker logs jenkins-python `

Dans l’interface Jenkins (http://localhost:8080) :

Installer les plugins git, pipeline, etc.

Créer un nouveau « Pipeline » depuis SCM (URL de ton repo public).

Choisir Branche master.

Jenkins va exécuter le Jenkinsfile suivant :

````
pipeline {
    agent any
    stages {
        stage('📦 Installer les dépendances') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('🧪 Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }
    }
    post {
        always {
            echo '🎯 Pipeline terminé'
        }
    }
}
`````
Le pipeline s’exécutera à chaque push sur main. Les tests renvoyés sont des tests unitaires isolés (mock BDD), donc le job ne dépend plus d’une base réelle.

Partie 5 : Livrables
Code source : ce dépôt GitHub public .

README.md : instructions détaillées (ce fichier).

Jenkinsfile : présent à la racine pour CI/CD.

Scripts MySQL : mysql-init/init.sql pour initialisation (local).

Tests : test/test_articles.py (unitaire).


✔️ Validation
Architecture du code : OK (app + config séparés).

Gestion des configurations : OK (config.py).

Documentation : ce README décrit tout.

MySQL en local : OK (via Docker Compose + init.sql).

Tests unitaires : OK (mock).

Pipeline CI/CD : OK (Jenkins en Docker, Jenkinsfile, tests passés sans BDD réelle).