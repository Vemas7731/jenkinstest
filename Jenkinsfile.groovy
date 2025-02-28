pipeline {
    agent any

    environment {
        DISCORD_WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1344552070253908008/cb713-OKHK1-h0ReOPTp97mbbC1X4Tlsxj52c4F0knz7LJD0FslDoDuSmb6_NAlmomxG'
        SCANNER_HOME = tool 'Sonarscanner' // Sesuaikan dengan nama scanner
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

        stage('SonarCloud Analysis') {
            steps {
                script {
                    sh '''
                    sonar-scanner \
                      -Dsonar.projectKey=Vemas7731_jenkinstest \
                      -Dsonar.organization=vemas7731 \
                      -Dsonar.sources=. \
                      -Dsonar.host.url=https://sonarcloud.io \
                      -Dsonar.login=004ff33f53154da4086b27ea56cf9cd234a13449
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    timeout(time: 1, unit: 'MINUTES') {
                        waitForQualityGate abortPipeline: true
                    }
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
                     -d '{ "content": "✅ Jenkins Pipeline Succeeded! SonarQube Passed 🎉" }' \\
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
                     -d '{ "content": "❌ Jenkins Pipeline Failed! SonarQube Issues Found ⚠️" }' \\
                     "$DISCORD_WEBHOOK_URL"
                """
            }
        }
    }
}
