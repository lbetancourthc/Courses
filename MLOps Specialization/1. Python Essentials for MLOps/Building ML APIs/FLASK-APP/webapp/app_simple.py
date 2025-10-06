from flask import Flask, abort


app = Flask("Flask App")

@app.route("/")
def two_hundred():
    return "200... All is well..."

@app.route("/error")
def error():
    abort(500, "Something went wrong...")


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")