pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Vemas7731/jenkinstest.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install pandas
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                sh '''
                source venv/bin/activate
                python anjay2.py  # Ganti dengan nama script Python yang ingin dijalankan
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }

    post {
        success {
            sh '''
            curl -H "Content-Type: application/json" \
                 -X POST \
                 -d '{"username": "Jenkins", "content": "✅ Pipeline SUCCESS! 🎉"}' \
                 https://discordapp.com/api/webhooks/1344552070253908008/cb713-OKHK1-h0ReOPTp97mbbC1X4Tlsxj52c4F0knz7LJD0FslDoDuSmb6_NAlmomxG
            '''
        }
        failure {
            sh '''
            curl -H "Content-Type: application/json" \
                 -X POST \
                 -d '{"username": "Jenkins", "content": "❌ Pipeline FAILED! Check logs. 🚨"}' \
                 https://discordapp.com/api/webhooks/1344552070253908008/cb713-OKHK1-h0ReOPTp97mbbC1X4Tlsxj52c4F0knz7LJD0FslDoDuSmb6_NAlmomxG
            '''
        }
    }
}
