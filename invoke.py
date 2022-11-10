from threading import Thread

from flask import Flask
import main

app = Flask(__name__)


@app.route('/start')
def start():
    Thread(target=main.main()).start()
    return "Started"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
