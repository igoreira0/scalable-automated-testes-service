import os

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = int(os.getenv('REDIS_PORT'))
REDIS_PASS = os.getenv('REDIS_PASS')
REDIS_USER = os.getenv('REDIS_USER')
REDIS_TEST_DB = int(os.getenv('REDIS_TEST_DB', '1'))

TEST_KEY = os.getenv('TEST_KEY', 'test')

MONGODB_DATABASE = os.getenv('MONGO_TEST_DATABASE')
MONGODB_TESTS_COLLECTION = os.getenv('MONGODB_TEST_COLLECTION')
MONGO_URI = os.getenv('MONGO_URI')