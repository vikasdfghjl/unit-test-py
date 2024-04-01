pipeline {
    agent any

    stages {
        stage('Unit Tests') {
            steps {
                sh 'python -m unittest discover -v tests/'
            }
        }
    }

    post {
        always {
            junit '*.xml' // Collect any generated JUnit XML test reports
        }
    }
}
