pipeline {
	agent any

  stages {
		stage('Checkout') {
			steps {
				echo "📦 Clonage du dépôt"
        checkout scm
      }
    }

        stage('Install Python') {
  steps {
    echo "📦 Installation des dépendances"
    sh '''
      python --version
      python -m venv venv
      . venv/bin/activate
      pip install --upgrade pip
      pip install flask mysql-connector-python
    '''
  }
}


   stage('Tests') {
			steps {
				echo "🧪 Lancement des tests avec pytest"
              sh '''
                . venv/bin/activate || source venv/Scripts/activate
                pip install pytest
                chmod +x wait-for-it.sh
  				./wait-for-it.sh db pytest
                pytest
              '''
            }
   }




		stage('Build/Run') {
					steps {
						echo "🚀 Lancement de l'application"
			sh '''
			  . venv/bin/activate
			  python run.py &
			  sleep 5
			'''
		  }
		}

  }
  post {
		always {
			echo "🎯 Pipeline terminé"
    }
  }
}
