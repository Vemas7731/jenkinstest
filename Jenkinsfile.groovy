pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1344552070253908008/cb713-OKHK1-h0ReOPTp97mbbC1X4Tlsxj52c4F0knz7LJD0FslDoDuSmb6_NAlmomxG'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Vemas7731/jenkinstest.git'
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    echo 'Executing helloworld.py...'
                    sh 'python3 helloworld.py'
                }
            }
        }
    }

    post {
        success {
            script {
                echo 'Pipeline succeeded! Sending Discord notification...'
                sh """
                curl -H "Content-Type: application/json" \\
                     -X POST \\
                     -d '{ "content": "✅ Jenkins Pipeline Succeeded!" }' \\
                     "$DISCORD_WEBHOOK_URL"
                """
            }
        }
        failure {
            script {
                echo 'Pipeline failed! Sending Discord notification...'
                sh """
                curl -H "Content-Type: application/json" \\
                     -X POST \\
                     -d '{ "content": "❌ Jenkins Pipeline Failed!" }' \\
                     "$DISCORD_WEBHOOK_URL"
                """
            }
        }
    }
}
