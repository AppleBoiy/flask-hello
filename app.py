from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/greets', methods=['POST'])
def greeter():
    data = request.get_json()
    name = data["name"]
    return jsonify({"message": f"Hello {name}!"})

