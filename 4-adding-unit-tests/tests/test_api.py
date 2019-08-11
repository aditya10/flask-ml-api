import unittest
from api.app import app


class FlaskTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.post('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
