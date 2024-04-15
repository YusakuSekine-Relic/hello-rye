from flask import Flask

def main() -> int:
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"
    app.run()
    return 0
