from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

dbClient = MongoClient('mongodb://mongo:27017/')

db = dbClient['CoRiderTaskDB']
collection = db['users']

def format_id(user):
    user['_id'] = str(user['_id'])
    return user

@app.route('/users', methods=['GET'])
def getUsers():
    users = list(collection.find())
    return jsonify([format_id(user) for user in users]), 200

@app.route('/users/<string:id>', methods=['GET'])
def getUser(id):
    user = collection.find_one({"_id": ObjectId(id)})
    if user:
        return jsonify(format_id(user)), 200
    else:
        return jsonify({"error": "User not found"}), 404  

@app.route('/users', methods=['POST'])
def createUser():
    data = request.json
    required_fields = ["name", "email", "password"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400
    collection.insert_one(data)
    return jsonify({"message": "User created"}), 201

@app.route('/users/<string:id>', methods=['PUT'])
def updateUser(id):
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count > 0:
        return jsonify({"message": "User updated"}), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/users/<string:id>', methods=['DELETE'])
def deleteUser(id):
    result = collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count > 0:
        return jsonify({"message": "User deleted"}), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)