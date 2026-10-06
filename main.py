from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/")
def name():
    return "<h1> Hi, I am Pauline Moraa from Enterprise Web Dev!</h1>"
from flask import Flask


app = Flask(__name__)


MESSAGE = "my name is emma this enterprise web development i build a flask !"


@app.route("/")
@app.route("/name")
def name() -> str:
    return MESSAGE


if __name__ == "__main__":
    app.run(debug=True)