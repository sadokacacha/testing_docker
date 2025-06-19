FROM jenkins/jenkins:lts

USER root

# Replace 999 below with the GID from the previous step
RUN groupadd -g 974 docker && \
    usermod -aG docker jenkins && \
    apt-get update && \
    apt-get install -y docker.io

USER jenkins
