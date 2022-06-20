// Declarative //
pipeline {
    agent any
    stages {
        stage("check Docker env") {
            steps {
              bat '''
                docker version
                docker info
                docker compose version
            '''
            }
        }
    }
} 