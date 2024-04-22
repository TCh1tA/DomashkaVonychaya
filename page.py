from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<img src="static/Slave.jpg" alt="Ой)">'


# @app.route('/index')
# def yabloki():
#     return '<img src="data/Slave.jpg">'


if __name__ == "__main__":
    app.run('127.0.0.1', port=8080)
