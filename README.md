#  My Ecommerce Application Description
This project is an e-commerce application developed with Node.js, Express API, and MongoDB, and containerized using Docker. Each part of the application—the backend API, frontend client, and MongoDB database—is packaged into separate containers. These containers act as independent microservices and communicate through a dedicated Docker Bridge network called Gerrys_network. This setup streamlines dependency management, enhances scalability, and ensures uniformity between development and production environments. Docker Compose manages the orchestration of these containers, making the build and deployment processes straightforward.

# Requirements

Make sure that you have the following installed:


- [Node.js](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-18-04)

- npm

- [MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/) and start the MongoDB service with `sudo service mongod start`

- [Docker](https://docs.docker.com/get-docker/)

- [Docker Compose](https://docs.docker.com/compose/install/)


 # Setup Instructions

# Navigate to the Client Folder

 cd client

# Install Dependencies

npm install

# Start the Client Application

npm start

# Navigate to the Backend Folder
# Open a new terminal to be safer and run the following commands:

cd ../backend

# Install Backend Dependencies

npm install

# Start the Backend Application

npm start

# Running the Application
The application will be available at:

  Frontend: http://localhost:3000
  Backend: http://localhost:5000

  

