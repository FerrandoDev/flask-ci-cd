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
