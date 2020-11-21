from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask"

@app.route("/test")
def test():
    return "I am a test"

@app.route("/user/<user_name>")
def log_in(user_name):
    return "Hello " + user_name

if __name__ == "__main__":
    app.run()