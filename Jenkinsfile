pipeline {
    agent any

    stages {
        stage('ATG Connection Test') {
            steps {
                sh '''python -m unittest -v test_atg_connection.py''' 
            }
        }
    }

    post {
        always {
            junit '*.xml' // Collect any generated JUnit XML test reports
        }
    }
}
