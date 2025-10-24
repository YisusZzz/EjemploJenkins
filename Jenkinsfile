pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/YisusZzz/EjemploJenkins.git'  
            }
        }
        stage('Build') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                bat 'python -m pytest --junitxml=test-reports/results.xml'
            }
        }
        stage('Report') {
            steps {
                junit 'test-reports/results.xml'
            }
        }
    }
    post {
        always {
            echo 'Pipeline terminado.'
        }
        success {
            echo 'Todas las pruebas pasaron exitosamente.'
        }
        failure {
            echo 'Alguna prueba falló.'
        }
    }
}