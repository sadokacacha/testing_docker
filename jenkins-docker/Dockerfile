FROM jenkins/jenkins:lts

USER root




RUN groupadd -g 974 docker && \
    usermod -aG docker jenkins && \
    apt-get update && \
    apt-get install -y docker.io

USER jenkins
