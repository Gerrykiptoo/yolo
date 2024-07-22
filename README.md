#  My Ecommerce Application Description
This project is an e-commerce application developed with Node.js, Express API, and MongoDB, and containerized using Docker. Each part of the application—the backend API, frontend client, and MongoDB database—is packaged into separate containers. These containers act as independent microservices and communicate through a dedicated Docker Bridge network called Gerrys_network. This setup streamlines dependency management, enhances scalability, and ensures uniformity between development and production environments. Docker Compose manages the orchestration of these containers, making the build and deployment processes straightforward.
