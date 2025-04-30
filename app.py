from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/") # root url
def home():
    return "<h1>Weolcome to our first awesome Flask application!</h1><p>Home Page</p>" 

@app.route("/api/status")
def status():
    return jsonify ({
            "status" : "OK",
            "message" : "Server running",
            "version" : "1.0"
        }
    )

@app.route("/parameters/sum/<int:x>/<int:y>") # handling parameters
def sum(x, y):
    return jsonify ({
            "result" : x + y,
        }
    )

if __name__ == "__main__":
    app.run(debug=True)