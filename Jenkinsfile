pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                sh 'echo "heello"'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t django-${GIT_BRANCH}-1.0.0:${BUILD_NUMBER} .'
            }
        }
        stage('Test') {
            steps {
                sh './manage.py test' 
            }
        }
        stage('Deploy') {
            steps {
                sh ''' 
                containers=$(docker ps | grep api* | awk '{print $1}')
                if [ ! -z $containers ];
                then
	                docker container stop $containers
                fi
                ''' 
                sh 'docker run -d -p 3000:3000 api-${GIT_BRANCH}-1.0.0:${BUILD_NUMBER}'
            }
        }
    }
}