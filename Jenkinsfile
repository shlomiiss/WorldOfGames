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
        stage("bulid using Docker Compose"){
          steps {
            //bat "docker build -t test/wog11 ."
            bat "docker compose up -d --no-start"
      } 
        stage("Start the Game Container"){
          steps {
            //bat "docker build -t test/wog11 ."
            bat "docker compose up -d WogGame"
            bat "docker ps"
       }
         stage("Testing "){
           steps {
            //bat "docker build -t test/wog11 ."
             bat "echo tests"
           }
        stage("Final "){
           steps {
            bat "docker compose down"
            bat "docker compose push wog"
         }
        }
      }
    } 
  }
 }
}
