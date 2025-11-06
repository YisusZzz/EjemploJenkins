pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YisusZzz/EjemploJenkins.git'
            }
        }
        stage('Build') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                // Asegurarse de que el directorio exista antes de escribir en él
                bat 'mkdir test-reports || echo "Directorio ya existe"'
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
