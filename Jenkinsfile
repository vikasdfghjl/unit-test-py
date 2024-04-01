pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                // Install any dependencies required for your tests
                sh 'apt install python3'
                sh 'python3 --version'
                sh 'pip3 install -r requirements.txt' 
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
