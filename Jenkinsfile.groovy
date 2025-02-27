pipeline {
    agent any  // Menjalankan pipeline di agent mana saja
    stages {
        stage('Checkout') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    git branch: 'main', url: 'https://github.com/Vemas7731/jenkinstest.git'
                }
            }
        }
        stage('Build') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'echo "Building project..."'
                }
            }
        }
        stage('Test') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'echo "Running tests..."'
                }
            }
        }
        stage('Deploy') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    sh 'echo "Deploying application..."'
                }
            }
        }
    }
    post {
        failure {
            sh 'echo "Pipeline failed! Check logs for details."'
        }
    }
}
