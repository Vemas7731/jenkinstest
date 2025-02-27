pipeline {
    agent any  // Menjalankan pipeline di agent Jenkins mana saja
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Vemas7731/jenkinstest.git'  // Ambil kode dari Git
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Building project..."'  // Contoh build sederhana
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running tests..."'  // Jalankan testing
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying application..."'  // Simulasi deployment
            }
        }
    }
}
