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
					
					# Attend jusqu'à 2 minutes que la BDD soit prête
					max_wait=120
					count=0
					while [ "$count" -lt "$max_wait" ]; do
						status=$(docker inspect --format '{{.State.Health.Status}}' mysql_db)
						if [ "$status" == "healthy" ]; then
							echo "✅ Base de données prête."
							break
						fi
						echo "En attente de la BDD (statut: $status)..."
						sleep 5
						count=$((count + 5))
					done

					if [ "$status" != "healthy" ]; then
						echo "❌ La base de données n'a pas démarré à temps."
						exit 1
					fi

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
