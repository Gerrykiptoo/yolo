##  My Ecommerce Application Description
This project is an e-commerce application developed with Node.js, Express API, and MongoDB, and containerized using Docker. Each part of the application—the backend API, frontend client, and MongoDB database—is packaged into separate containers. These containers act as independent microservices and communicate through a dedicated Docker Bridge network called Gerrys_network. This setup streamlines dependency management, enhances scalability, and ensures uniformity between development and production environments. Docker Compose manages the orchestration of these containers, making the build and deployment processes straightforward.

## Table of content
## Requirements
Setup Instructions
Running the Application
Running with Docker
Pushing Docker Images to Docker Hub
Ansible Deployment
Vagrant Configuration
Google Cloud SDK (for Kubernetes deployment)
Kubectl (for Kubernetes deployment)
## Requirements

Make sure that you have the following installed:


- [Node.js](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-18-04)

- npm

- [MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/) and start the MongoDB service with `sudo service mongod start`

- [Docker](https://docs.docker.com/get-docker/)

- [Docker Compose](https://docs.docker.com/compose/install/)

- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)

- [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

 ## Setup Instructions

## Navigate to the Client Folder

 cd client

## Install Dependencies

npm install

## Start the Client Application

npm start

## Navigate to the Backend Folder
## Open a new terminal to be safer and run the following commands:

cd ../backend

## Install Backend Dependencies

npm install

## Start the Backend Application

npm start

##  Running the Application
The application will be available at:

- The backend service will be accessible at [http://localhost:5000](http://localhost:5000).
- The frontend service will be accessible at [http://localhost:3000](http://localhost:3000).

  

##  Running with Docker

## Build the Docker images:

sudo docker compose build

# Start the containers:
 
sudo docker compose up
 
 ## Push the Docker images to Docker Hub:

docker login

docker tag frontend-img:v1.0.0 gerrykiptoo/frontend:v1.0.0

docker tag backend-img:v1.0.0 gerrykiptoo/backend:v1.0.0

docker push gerrykiptoo/frontend:v1.0.0

docker push gerrykiptoo/backend:v1.0.0

## Ansible Deployment

## Playbook
The Ansible playbook (playbook.yml) is used to provision Docker containers for the backend, frontend, and MongoDB services. It includes tasks from roles defined for each of these services.
here is a clue of the playbook
---
- name: Provision Docker Containers
  hosts: all
  vars_files:
    - /vagrant/vars/vars.yml
  roles:
    - backend
    - frontend
    - mongodb

## Hosts File

The hosts file specifies the SSH connection details for Ansible to connect to the Vagrant virtual machines for the backend, frontend, and MongoDB services.

[backend]
backend_host ansible_host=127.0.0.1 ansible_port=2202 ansible_user=vagrant ansible_private_key_file=.vagrant/machines/backend/virtualbox/private_key

[frontend]
frontend_host ansible_host=127.0.0.1 ansible_port=2222 ansible_user=vagrant ansible_private_key_file=.vagrant/machines/frontend/virtualbox/private_key

[mongo]
mongo_host ansible_host=127.0.0.1 ansible_port=2201 ansible_user=vagrant ansible_private_key_file=.vagrant/machines/mongo/virtualbox/private_key


## Vagrant Configuration

The Vagrantfile is configured to set up three VMs for the frontend, backend, and MongoDB services. Each VM has its ports forwarded and is provisioned using Ansible.


## Kubernetes Deployment

1. Configure Kubernetes Cluster

Ensure that you have a GKE cluster running and that your kubectl is 
configured to communicate with the cluster.
# Create a GKE cluster:
using the commands bellow:

gcloud container clusters create yolo-cluster --num-nodes=2 --zone=us-central1-a

 2. Configure kubectl to use the GKE cluster:
 by using the command below

gcloud container clusters get-credentials yolo-cluster --zone us-central1-a --project your-project-id


## Deploy Your Application

 My Kubernetes manifests (for backend, frontend, and MongoDB) are stored in the manifest directory.


# Deploy MongoDB:
using the command below:

kubectl apply -f manifest/mongo.yaml

# Deploy the Backend:
using the command below:
kubectl apply -f manifest/backend.yaml

# Deploy the Frontend:
using the command below:
kubectl apply -f manifest/frontend.yaml




