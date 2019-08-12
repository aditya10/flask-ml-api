import unittest
import json
from flask import Flask
from api.endpoints.classification import classification_api

app = Flask(__name__)
app.register_blueprint(classification_api)


class ClassificationTests(unittest.TestCase):

    tester = None

    def __init__(self, *args, **kwargs):
        super(ClassificationTests, self).__init__(*args, **kwargs)
        global tester
        tester = app.test_client()

    def test_classify_single(self):
        response = tester.get(
            '/classification',
            data=json.dumps({"text": "Cocoa setup issues"}),
            content_type='application/json'
        )

        data = response.get_data(as_text=True)
        print("Category predicted: "+str(data))
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(data)


if __name__ == '__main__':
    unittest.main()
