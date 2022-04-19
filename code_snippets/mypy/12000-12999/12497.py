# temp.py
import flask

app = flask.Flask("name")

@app.route("/")
def home() -> flask.Response:
    return f""
