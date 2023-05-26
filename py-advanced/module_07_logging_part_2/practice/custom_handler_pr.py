import logging
import sys


class CustomHandlerPr(logging.Handler):

    def __init__(self, file_name, mode='a'):
        super().__init__()
        self.file_name = file_name
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        print('my custom handler', msg)
        with open(self.file_name, self.mode) as kek:
            kek.write(msg + '\n')


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },
        'flow': {
            "()": CustomHandlerPr,
            "level": "DEBUG",
            "formatter": "base",
            "file_name": 'pr_log_1.log',
            "mode": 'a'
        }
    },
    "loggers": {
        "module_logger": {
            "level": "DEBUG",
            "handlers": ["flow", 'console'],
            # "propagate": False
        }
    },
    # "filters": {},
    # "root": {} # == "": {}
}
