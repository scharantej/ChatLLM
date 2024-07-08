
# main.py

from flask import Flask, request, render_template
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    message = request.get_json()
    response = process_message(message["message"])
    return json.dumps({"message": response})


@app.route("/resources/<path:path>")
def resources(path):
    return send_from_directory("resources", path)


def process_message(message):
    # Your custom message processing logic goes here
    # For example, you could use a LLM to generate a response
    response = "Hello, " + message
    return response


if __name__ == "__main__":
    app.run()
