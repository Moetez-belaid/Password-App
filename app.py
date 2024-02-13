from flask import Flask

First_app = Flask(__name__)

@First_app.route("/")
def hello():
    return "hello world! Moetez test "

if __name__ == "__main__":
    First_app.run(debug=True , port=9000)
    