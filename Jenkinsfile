pipeline {
    agent { label 'centos7-docker-8c-8g' }
    environment {
        SECURITY_SERVICE_NEEDED = false
    }
    stages {
        stage('Prep') {
            steps {
                script {
                    sh 'curl -v https://raw.githubusercontent.com/edgexfoundry/developer-scripts/master/releases/geneva/compose-files/docker-compose-geneva-mongo-no-secty.yml > docker-compose.yml'
                    docker
                        .image('nexus3.edgexfoundry.org:10003/edgex-devops/edgex-compose:latest')
                        .inside('-u 0:0 --entrypoint= --net host --security-opt label:disable -v /var/run/docker.sock:/var/run/docker.sock')
                    {
                        sh 'docker ps -a'
                        sh 'docker-compose up -d'
                        sh 'sleep 60'
                        sh 'docker ps -a'
                    }
                }
            }
        }

        stage('CIS Benchmark') {
            steps {
                sh 'docker run --net host --pid host --cap-add audit_control -e DOCKER_CONTENT_TRUST=$DOCKER_CONTENT_TRUST -v /var/lib:/var/lib -v /var/run/docker.sock:/var/run/docker.sock -v /usr/lib/systemd:/usr/lib/systemd -v /etc:/etc --label docker_bench_security docker/docker-bench-security'
            }
        }
    }
}
