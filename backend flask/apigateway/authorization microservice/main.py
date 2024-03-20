from flask import Flask, request, jsonify

app = Flask(__name__)

data = data = {
    "message": "Hi from authorization microservice"
}


@app.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def hello_world():
    print(request.method)
    if request.method == "GET":
        return jsonify(data)

    else:
        return "ERROR", 404


if __name__ == '__main__':
    app.run(port=5002, debug=True)
