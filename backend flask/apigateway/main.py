from flask import Flask, request
import requests
import json
app = Flask(__name__)


@app.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def hello_world():
    if request.method == "GET":
        return "<p>Hello, World from api gateway!</p>"

    else:
        return "ERROR"


@app.route("/<microservice>", methods=["GET", "POST", "PUT", "DELETE"])
def microservice(microservice):

    if request.method == "GET":

        if microservice == "authorization":
            # response = requests.get('http://127.0.0.1:5002')
            response = requests.post('http://127.0.0.1:5002')
            if response.status_code == 200:
                data = response.json()
            else:
                return "invalid request", 404
        elif microservice == "training":
            # response = requests.get('http://127.0.0.1:5001')
            response = requests.post('http://127.0.0.1:5002')
            if response.status_code == 200:
                data = response.json()
            else:
                return "invalid request", 404

        elif microservice == "datahandling":
            # response = requests.get('http://127.0.0.1:5003')
            response = requests.post('http://127.0.0.1:5002')
            if response.status_code == 200:
                data = response.json()
            else:
                return "invalid request", 404

            data = response.json()

    else:
        return "ERROR", 404

    return data


if __name__ == '__main__':
    app.run(port=5000, debug=True)
