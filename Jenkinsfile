pipeline {
     agent {label "agent01"}
     stages {
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
             //bat "docker compose up -d"
             bat "docker compose -f docker-compose_volume.yml up -d"
             //bat "docker ps"
          }
         }
           stage("Testing flask "){
           steps {
            script{
             //bat "docker exec -it TheGame"
             //bat "python /tests/e2e.py"
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
              bat "docker compose -f docker-compose_prod.yml down"
              sleep(time:1,unit:"MINUTES")
              bat "docker compose -f docker-compose_prod.yml up -d --no-start"
              sleep(time:1,unit:"MINUTES")
              //bat "docker compose push ."
              bat "docker push 24912491/worldofgames-wog-1/wog43"
            }
           }
          }
        }