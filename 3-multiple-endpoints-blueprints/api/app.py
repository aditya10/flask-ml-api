from flask import Flask
from .endpoints.classification import classification_api

app = Flask(__name__)
app.register_blueprint(classification_api)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
