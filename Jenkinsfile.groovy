pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Vemas7731/jenkinstest.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    echo 'Building...'
                    sh 'echo "Build success!"'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    sh 'echo "All tests passed!"'
                }
            }
        }
    }

    post {
        success {
            script {
                echo 'Pipeline executed successfully!'
            }
        }
        failure {
            script {
                echo 'Pipeline failed!'
                sh 'echo "Sending failure notification..."'
            }
        }
    }
}
