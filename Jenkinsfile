pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip3 install django'
                sh 'docker build -t django-${GIT_BRANCH}-1.0.0:${BUILD_NUMBER} .'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 manage.py test' 
            }
        }
        stage('Deploy') {
            steps {
                sh ''' 
                containers=$(docker ps | grep django* | awk '{print $1}')
                if [ ! -z $containers ];
                then
	                docker container stop $containers
                fi
                ''' 
                sh 'docker run -d -p 3000:3000 django-${GIT_BRANCH}-1.0.0:${BUILD_NUMBER}'
            }
        }
    }
}