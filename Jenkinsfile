pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                // Install any dependencies required for your tests
                sh 'export PATH=$PATH:/usr/bin/python3'
                sh 'pip install -r requirements.txt' 
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest -v test_atg_connection.py'
            }
        }

        stage('Collect Results') {
            steps {
                junit '*.xml' // Collect any JUnit-format test reports
            }
        }
    }
}
