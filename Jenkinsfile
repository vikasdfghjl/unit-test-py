pipeline {
    agent any

    stages {
        stage('Unit Tests') {
            steps {
                sh 'python3 -m unittest test_atg_connection.py'
            }
        }
    }

    post {
        always {
            junit '*.xml' // Collect any generated JUnit XML test reports
        }
    }
}
