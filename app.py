from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Flask app is running successfully",
        "status": "OK"
    })

@app.route("/health")
def health():
    return jsonify({
        "service": "flask-basic-app",
        "health": "healthy"
    })

@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello from Flask inside Docker"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
