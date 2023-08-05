
import logging


class MockLoggingHandler(logging.Handler):
    """Mock logging handler that accumulates expected log messages."""

    def __init__(self, *args, **kwargs):
        self.messages = {}

        self.reset()
        logging.Handler.__init__(self, *args, **kwargs)

    def emit(self, record):
        self.messages[record.levelname.lower()].append(record.getMessage())

    def reset(self):
        self.messages = {
            'debug': [],
            'info': [],
            'warning': [],
            'error': [],
            'critical': [],
        }
