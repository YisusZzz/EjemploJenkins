pipeline {
    agent any
    
    environment {
        // Esto está perfecto, lo dejamos como está
        PATH = "C:\\Users\\olake\\AppData\\Local\\Programs\\Python\\Python314;${env.PATH}"
    }
    
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
        
        // --- CORRECCIÓN AQUÍ ---
        stage('Test') {
            steps {
                // Esta es la forma más segura de crear el directorio:
                // "Si NO EXISTE 'test-reports', entonces CREA 'test-reports'"
                // Este comando nunca fallará.
                bat 'if not exist test-reports mkdir test-reports'
                
                // Ahora que el comando anterior no falla,
                // Jenkins continuará y ejecutará este comando de pruebas.
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
