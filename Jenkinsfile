pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest tests\\lesson_23\\test_car_api.py --junitxml=results.xml'
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
    }

    post {
        success {
            echo 'Тести успішно пройшли!'
        }
        failure {
            echo 'Тести не пройшли!'
        }
    }
}
