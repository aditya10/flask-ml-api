from flask import Blueprint, request, jsonify
from fastai.text import *
import json

classification_api = Blueprint('classification_api', __name__)

learner = load_learner('api/models/', 'classification.pkl')


@classification_api.route("/classification")
def classification():
    sample = json.loads(request.data)["text"]
    return jsonify(str(learner.predict(sample)[0]))
