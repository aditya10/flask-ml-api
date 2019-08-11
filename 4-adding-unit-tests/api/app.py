from flask import Flask
import logging
from .endpoints.names import names_api

app = Flask(__name__)
app.register_blueprint(names_api)


@app.route("/")
def hello():
    return "Hello World"


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
