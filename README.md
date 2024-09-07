# Feed App - Post Service

This project is a microservice architecture implementation for managing user posts, comments, likes, and followers in a feed application. The application is built using Flask and MySQL, following a clean code and SOLID principles. The service includes the following key features:

- **Post Service**: Handles creating, updating, retrieving, and deleting user posts.
- **Comment Service**: Allows users to comment on posts.
- **Like Service**: Enables users to like posts.
- **Following Service**: Manages user follow relationships.

## Database Diagrams

The following are the database structure diagrams for the various services:

### User Service

![User Service](https://github.com/ehapsamy0/feed_app/blob/post-service-init/erd/user_service.jpeg)

### Post Service

![Post Service](https://github.com/ehapsamy0/feed_app/blob/post-service-init/erd/post_service.jpeg)

### Following Service

![Following Service](https://github.com/ehapsamy0/feed_app/blob/post-service-init/erd/following_service.jpeg)

## Project Structure

The project is structured as a set of independent microservices, with each service responsible for handling specific functionality.




### Key Technologies
- **Python** (Flask)
- **MySQL** for data storage
- **Docker** for containerization
- **Ruff** for linting and code quality

## Getting Started

To get started with this project, follow the instructions below:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ehapsamy0/feed_app.git
   cd feed_app


2. **Run the application with Docker**:
   ```bash
   docker-compose up --build
   

3. **Access the API**:
The API will be running on `http://localhost:5000`. You can use tools like `Postman` or `curl` to interact with the API