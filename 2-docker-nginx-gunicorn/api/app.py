from flask import Flask, jsonify, request
from fastai.text import *
import json

app = Flask(__name__)

learner = load_learner('api/', 'export.pkl')


@app.route("/classification")
def classification():
    sample = json.loads(request.data)["text"]
    return jsonify(str(learner.predict(sample)[0]))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
