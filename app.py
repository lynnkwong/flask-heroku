import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    app_name = os.environ.get("APP_NAME", "My App")
    return f"<h1>Hello from {app_name}!<h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
