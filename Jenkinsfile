pipeline {
	agent any

  stages {
		stage('Checkout') {
			steps {
				echo "📦 Clonage du dépôt"
        checkout scm
      }
    }

        stage('Tests') {
			steps {
				echo "🧪 Lancement des tests avec docker-compose"
				sh '''
					docker-compose up --build -d db
					echo "Attente de la base de données..."
					sleep 15
					docker-compose run --rm app pytest
				'''
			}
		}

		stage('Build Image') {
			steps {
				echo "📦 Construction de l'image de l'application"
				sh 'docker-compose build app'
			}
		}

  }
  post {
		always {
			echo "🧹 Nettoyage des conteneurs"
			sh 'docker-compose down -v --remove-orphans'
			echo "🎯 Pipeline terminé"
    }
  }
}
