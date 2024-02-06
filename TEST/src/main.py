from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def helloworld():
    return send_file("../static/install.gif", mimetype="image/gif")


@app.route("/test")
def test():
    return send_file("../static/ci.png", mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
