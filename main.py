from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<center><h1>Flask App deployment on AZURE</h1></center>"

if __name__ == "__main__":
    app.run()
    