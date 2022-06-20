#to
#I should add env for Docker on the loca host
pipeline {
  agent any
    stages {
      stage ('check docker env '){
       steps {
         sh '''
           docker version
           docker info
           docker compose version
           curl --version
           '''
           }
         }
  }
}