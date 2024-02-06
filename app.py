from flask import Flask

app = Flask(__name__)


@app.route("/")
def helloworld():
    return "Hello, World!"


@app.route("/test")
def test():
    return "capitalize test"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
