pipeline {
    agent any
    environment {
        GIT_REPO = 'https://github.com/Linzpe/Pipeline_Jenkins.git'
        BRANCH = 'main'
        CREDENTIALS_ID = 'github-credentials-id' // El ID de las credenciales configuradas en Jenkins
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: "${BRANCH}", credentialsId: "${CREDENTIALS_ID}", url: "${GIT_REPO}"
                }
            }
        }
        stage('Build') {
            steps {
                sh '''
                    python Test.py
                '''
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
