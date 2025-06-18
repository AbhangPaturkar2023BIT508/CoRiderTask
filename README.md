
## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-mongodb-crud-api.git
cd flask-mongodb-crud-api
2. Start the Application with Docker
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