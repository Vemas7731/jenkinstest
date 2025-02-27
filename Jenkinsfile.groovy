pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'SonarQube' // Sesuaikan dengan nama tool di Jenkins
    }

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

        stage('Install Dependencies') {
            steps {
                script {
                    sh '''
                        python3 -m venv venv
                        bash -c "source venv/bin/activate && pip install --upgrade pip && pip install pandas numpy matplotlib seaborn"
                    '''
                }
            }
        }

        stage('Execute Python Script') {
            steps {
                script {
                    sh '''
                        bash -c "source venv/bin/activate && python helloworld.py"
                    '''
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    withSonarQubeEnv('sonar-server') {
                        withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_AUTH_TOKEN')]) {
                            sh '''
                                ${SCANNER_HOME}/bin/sonar-scanner \
                                -Dsonar.projectKey=tes \
                                -Dsonar.projectName=tes \
                                -Dsonar.sources=. \
                                -Dsonar.host.url=https://sonarcloud.io \
                                -Dsonar.login=${SONAR_AUTH_TOKEN} \
                                -Dsonar.organization=muhammadrezaalfatah
                            '''
                        }
                    }
                }
            }
        }

        stage('Quality Gate') {
            steps {
                script {
                    def qg = waitForQualityGate()
                    if (qg.status != 'OK') {
                        error "Quality Gate Failed: ${qg.status}"
                    }
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
        success {
            sh 'curl -X POST -H "Content-Type: application/json" -d \'{"username": "Jenkins", "content": "✅ Pipeline SUCCESS! 🎉"}\' https://discordapp.com/api/webhooks/1344552070253908008/cb713-OKHK1-h0ReOPTp97mbbC1X4Tlsxj52c4F0knz7LJD0FslDoDuSmb6_NAlmomxG'
        }
        failure {
            sh 'curl -X POST -H "Content-Type: application/json" -d \'{"username": "Jenkins", "content": "❌ Pipeline FAILED! Check logs. 🚨"}\' https://discordapp.com/api/webhooks/1344552070253908008/cb713-OKHK1-h0ReOPTp97mbbC1X4Tlsxj52c4F0knz7LJD0FslDoDuSmb6_NAlmomxG'
        }
    }
}
