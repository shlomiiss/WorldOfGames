pipeline {
     agent {label "agent01"}
     stages {
         stage("bulid using Docker Compose") {
           steps {
             bat "docker compose -f docker-compose_volume.yml up -d --no-start"
          }
         }
         stage("Start the Game Container"){
           steps {
             bat "docker compose -f docker-compose_volume.yml up -d"
             bat "docker ps"
          }
         }
           stage("Testing flask "){
           steps {
            script{
              def s1 = bat(script:  "python ${WORKSPACE}/tests/e2e.py",returnStatus  : true)
              if (s1 != 0){
                currentBuild.result = "ABORTED"
                error ('The test failed. Stopping the pipeline')
               }
              }
            }
           }
         stage("Final - Push final image to GitHub ") {
           steps {
              bat "docker compose -f docker-compose_volume.yml down"
              bat "docker login -u 24912491 -p cd53f383-b699-4a02-a75b-c5ef834225be"
              bat "docker image tag wog46 24912491/worldofgames-wog-1:latest"
              bat "docker push 24912491/worldofgames-wog-1:latest"
            }
           }
          }
        }