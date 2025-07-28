pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/AlexanderOvch/AQA_Python.git', branch: 'main'
            }
        }
        stage('Install dependencies') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest lesson_09\\test_homeworks09.py --junitxml=results.xml'
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
    }

    post {
        always {
            echo 'Тест завершенo'
            emailext (
                to: 'featar@gmail.com',
                subject: "Build #${BUILD_NUMBER} - ${currentBuild.currentResult}",
                body: "Build finished with status: ${currentBuild.currentResult}"
            )
        }
        success {
            echo 'Тести успішно пройшли!'
        }
        failure {
            echo 'Тести не пройшли!'
        }
    }
}
