import logging
import time

from fluent import sender
from fluent import event

# Configure the Fluentd logger
logger = logging.getLogger('fluent.test')
logger.setLevel(logging.INFO)

fluent_handler = sender.FluentSender('app', host='fluentd', port=24224)
logger.addHandler(fluent_handler)

# Sample logging messages
def main():
    while True:
        logger.info('app.follow', {'message': 'Hello Fluentd!'})
        time.sleep(5)

if __name__ == "__main__":
    main()

