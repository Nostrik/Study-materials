import logging


class CustomHandlerForTaskFiveModuleSeven(logging.Handler):

    def __init__(self, file_name, mode='a'):
        super().__init__()
        self.file = file_name
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        with open(self.file, mode=self.mode) as log_file:
            log_file.write(msg + '\n')


config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(asctime)s - %(levelname)s - (%(message)s) - [%(name)s | %(module)s]"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },
        "file": {
            "()": CustomHandlerForTaskFiveModuleSeven,
            "level": "DEBUG",
            "formatter": "base",
            "file_name": "task_five_mod_seven.log",
            "mode": "a"
        },
        "rotating_time_handler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "base",
            "filename": "logging_at_10.log",
            "when": "H",
            "interval": 10,
            "backupCount": 0
        }
    },
    "loggers": {
        "main": {
            "level": "DEBUG",
            "handlers": ["console", "rotating_time_handler"]
        },
        "http_utils": {
            "level": "INFO",
            "handlers": ["console", "rotating_time_handler"]
        },
        "subprocess_utils": {
            "level": "INFO",
            "handlers": ["console", "rotating_time_handler"]
        }
    }
}
