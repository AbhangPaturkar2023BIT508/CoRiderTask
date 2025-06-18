# CoRider Task – Flask + MongoDB CRUD API (Dockerized)

This project is a simple RESTful CRUD API built using **Flask** and **MongoDB**, designed for the CoRider task submission. It is fully containerized using **Docker** and **Docker Compose**.

---

## Project Structure

CoRider/
├── app.py # Main Flask application
├── Dockerfile # Flask app container definition
├── docker-compose.yml # Multi-container setup (Flask + MongoDB)
├── requirements.txt # Python dependencies
└── README.md # This file

## Requirements

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)
- No need for Python or MongoDB to be installed locally

## Getting Started

### 1. Clone the Repository

-git clone https://github.com/your-username/corider-task.git
-cd corider-task 2. Build and Start the Containers
-docker-compose up --build
 Flask API will be available at: http://localhost:5000

 API Endpoints
Method Endpoint Description

GET /users Get all users
GET /users/<id> Get a specific user
POST /users Create a new user
PUT /users/<id> Update an existing user
DELETE /users/<id> Delete a user
