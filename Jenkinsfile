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
        stage("bulid"){
          steps {
            //bat "docker build -t test/wog11 ."
            bat "docker compose up -d --no-start"
      } 
    }
 } 
}