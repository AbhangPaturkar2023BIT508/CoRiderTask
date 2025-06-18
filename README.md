# Flask MongoDB CRUD REST API (Dockerized)

This is a simple Flask application that provides REST API endpoints for performing CRUD operations on a MongoDB database for a `User` resource.

## 🛠 Technologies Used

- Python 3.11
- Flask
- PyMongo (MongoDB client for Python)
- MongoDB
- Docker & Docker Compose

## 📦 User Resource Schema

Each User document in the database contains the following fields:

- `name` (string)
- `email` (string)
- `password` (string)

> Note: `_id` is automatically created by MongoDB as the unique identifier.

---

## 📂 Project Structure

.
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── Dockerfile # Docker image for Flask app
├── docker-compose.yml # Docker Compose setup for Flask + MongoDB
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-mongodb-crud-api.git
cd flask-mongodb-crud-api
2. Start the Application with Docker
bash
Copy
Edit
docker-compose up --build
Flask app will run on: http://localhost:5000

MongoDB runs in background on: mongodb://localhost:27017

🔗 API Endpoints
Method	Endpoint	Description
GET	/users	Get all users
GET	/users/<id>	Get a specific user by ID
POST	/users	Create a new user
PUT	/users/<id>	Update a user by ID
DELETE	/users/<id>	Delete a user by ID