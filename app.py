import logging
import json
import socket

class FluentdFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'host': socket.gethostname(),
            'where': record.module,
            'type': record.levelname,
            'message': record.getMessage(),
        }
        return json.dumps(log_record)

logger = logging.getLogger('fluent-bit-logger')
logger.setLevel(logging.INFO)
fluent_handler = logging.StreamHandler()
formatter = FluentdFormatter()
fluent_handler.setFormatter(formatter)
logger.addHandler(fluent_handler)

logger.info('Test log entry')
logger.error('This is an error message')
