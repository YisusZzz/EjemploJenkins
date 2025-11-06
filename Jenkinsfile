pipeline {
    agent any
    
    // --- Solución: Bloque de Entorno ---
    // Definimos un bloque de 'environment' (entorno)
    // para modificar la variable PATH del sistema ANTES de que se ejecuten las etapas.
    environment {
        // 1. Usamos tu ruta específica de Python.
        //    IMPORTANTE: En Groovy, las barras invertidas '\' 
        //    deben "escaparse" usando una doble barra '\\'.
        // 2. Agregamos tu ruta al INICIO del PATH existente (${env.PATH}),
        //    separada por un punto y coma ';'.
        PATH = "C:\\Users\\olake\\AppData\\Local\\Programs\\Python\\Python314;${env.PATH}"
    }
    
    stages {
        // Etapa 1: Descargar el código de la rama 'main'
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/YisusZzz/EjemploJenkins.git'
            }
        }
        
        // Etapa 2: Instalar dependencias
        stage('Build') {
            steps {
                // Jenkins ahora encontrará 'python.exe' porque 
                // agregamos la ruta al PATH en el bloque 'environment'.
                bat 'python -m pip install -r requirements.txt'
            }
        }
        
        // Etapa 3: Ejecutar pruebas
        stage('Test') {
            steps {
                // Creamos el directorio para los reportes si no existe
                bat 'mkdir test-reports || echo "Directorio ya existe"'
                
                // Ejecutamos pytest y le decimos que genere un reporte XML
                bat 'python -m pytest --junitxml=test-reports/results.xml'
            }
        }
        
        // Etapa 4: Publicar los resultados de las pruebas
        stage('Report') {
            steps {
                // Jenkins leerá el archivo XML y mostrará un gráfico de resultados
                junit 'test-reports/results.xml'
            }
        }
    }
    
    // Etapa 'post': Se ejecuta siempre al final
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
