import unittest

print("Running unit tests from api/tests directory...")

loader = unittest.TestLoader()
start_dir = 'api/tests'
suite = loader.discover(start_dir)

runner = unittest.TextTestRunner()
runner.run(suite)

print("Running tests is complete")
