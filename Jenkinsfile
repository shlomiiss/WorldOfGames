pipeline {
  agent any
    stages {
      stage ("check docker env")
         steps {
         sh '''
           docker version
           docker info
           docker compose version
             --version
           '''
             }
         }
    }