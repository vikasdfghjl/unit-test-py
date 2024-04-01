pipeline {
    agent any
    environment {
        HOME = "${env.WORKSPACE}"
    }
    tools{
        //dockerTool 'Docker'
        Python 'python3.10.12' 
     }

    stages {
        stage('Setup') {
            steps {
                // Install any dependencies required for your tests
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
