from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Sample data to be returned on a GET request
data = {
    "message": "Hi from the authorization microservice"
}

# MongoDB connection setup
db_connection = MongoClient('mongodb://rootuser:rootpass@localhost:27018/')
db_data_base = db_connection['user']
db_collection = db_data_base['user']

# Sample document to be inserted into MongoDB
data_db = {"name": "qazi", "age": 29, "password": 1234}


@app.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def hello_world():
    if request.method == "GET":
        # For demonstration, return a predefined message
        return jsonify(data)
    elif request.method == "POST":
        # Insert document into MongoDB on POST request
        inserted = db_collection.insert_one(data_db)
        string_id = str(inserted.inserted_id)

        return jsonify({"result": "Document inserted", "id": string_id}), 201
    else:
        # Placeholder for PUT and DELETE operations
        return "Method not supported", 405


if __name__ == '__main__':
    app.run(port=5002, debug=True)
