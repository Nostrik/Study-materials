import logging
import requests
import shlex
import subprocess


class CustomHandlerForTask8(logging.Handler):

    def __init__(self):
        super().__init__()
        self.server = "http://localhost:5000/log-entry"

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        proc = subprocess.Popen([f'curl -X POST {self.server} --data "msg={msg}"'], shell=True, stdout=subprocess.PIPE)


d_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s |"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },
        "server_pusher": {
            "()": CustomHandlerForTask8,
            "level": "DEBUG",
            "formatter": "base"
        }
    },
    "loggers": {
        "task_8_logger": {
            "level": "DEBUG",
            "handlers": ["console", "server_pusher"]
        }
    }
}