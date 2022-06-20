pipeline {
  agent any
    stages {
      stage ("check docker env")
       script{
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