from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Docker Auto-Build Lab!</h1><p>Your Flask application is running successfully inside a Docker container.</p>"

if __name__ == '__main__':
    # Listen on all interfaces at port 5000
    app.run(host='0.0.0.0', port=5000)
