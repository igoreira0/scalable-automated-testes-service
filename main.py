import logging
import redis
from config.tests import TESTS
import time
from utils.constants import TEST_KEY, REDIS_TEST_DB
from utils.queue_factory import create_queue_connection

redis = create_queue_connection(REDIS_TEST_DB)

def watch_queue():
    logging.info('Listening Queue')
    while True:
        message = redis.lpop(TEST_KEY)
        if(message):
            logging.info('Runing test %s', message.decode("utf-8"))
            instance = TESTS.get(int(message.decode("utf-8") ), None)()
            logging.info('instance for test %s has been created', instance.name)
            instance.run()
            logging.info('test %s ran', instance.name)
            instance.close()
            logging.info('test %s finished with %s', instance.name, instance.result)
            continue
        time.sleep(5)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info('Starting service...')
    watch_queue()
