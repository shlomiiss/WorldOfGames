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
        stage("bulid using Docker Compose") {
           steps {
            //bat "docker build -t test/wog25 ."
            //bat "docker compose up -d --no-start"
              bat "docker compose -f docker-compose_volume.yml up -d --no-start"

         } 
        } 
        stage("Start the Game Container"){
          steps {
            //bat "docker build -t test/wog27 ."
            bat "docker compose up -d"
            bat "docker ps"
         }
        }
         stage("Testing "){
           steps {
            //bat "docker build -t test/wog11 ."
             //docker exec -it TheGame
             //bat "python /tests/e2e.py
             def x = bat "(returnStdout: true , script: 'python /tests/e2e.py').trim()"
             script{
                      if (something) {
                            currentBuild.result = "FAILURE"
                            sh "exit 1"
             bat "echo tests"
             }
            }
           }
         }  
        stage("Final ") {
           steps {
            bat "docker compose down"
            sleep(time:1,unit:"MINUTES")
            bat "docker compose -f docker-compose_pro.yml up -d --no-start"
            sleep(time:1,unit:"MINUTES")
            bat docker compose push .
            //bat "docker push 24912491/worldofgames-wog-1:latest"
          }
        }
       }
     }
