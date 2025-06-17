// Jenkinsfile
pipeline {
    // 'agent any' means Jenkins will use any available agent
    // that matches its criteria. Since we'll run Jenkins itself
    // in Docker with the socket mounted, this works.
    agent any

    environment {
        // Define Docker Hub username as a pipeline environment variable
        // This is good practice for credentials
        DOCKER_HUB_USERNAME = 'sadokacacha' // Replace with your actual Docker Hub username
        IMAGE_NAME = 'flask-devops-dashboard'
    }

    stages {
        stage('Checkout') {
            steps {

                echo 'Repository checked out.'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker info'
                    sh "docker build -t ${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest -f Dockerfile ."
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // Use Jenkins' built-in credentials management
                    // Create a 'Username with password' credential in Jenkins later
                    // with ID 'dockerhub-credentials'
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "echo ${DOCKER_PASSWORD} | docker login -u ${DOCKER_USERNAME} --password-stdin"
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh "docker push ${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest"
                }
            }
        }
    }

    post {
        always {
            script {
                echo 'Cleaning up Docker image locally...'
                // Attempt to remove the built image locally after successful push
                // Use '|| true' to prevent script failure if image isn't found
                sh "docker rmi ${DOCKER_HUB_USERNAME}/${IMAGE_NAME}:latest || true"
                echo 'Pipeline finished.'
            }
        }
        failure {
            echo 'Pipeline failed. Check logs for errors.'
        }
    }
}