// Declarative //
pipeline {
    agent any
    stages {
        stage("check Docker env") {
            steps {
              sh '''
                docker version
                docker info
                docker compose version
            '''
            }
        }
    }
} 