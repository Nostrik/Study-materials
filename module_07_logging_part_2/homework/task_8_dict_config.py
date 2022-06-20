import logging
import sys
import shlex
import subprocess


class CustomHandlerForTask8(logging.Handler):

    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        # proc = subprocess.Popen([f'curl -X POST {self.server} --data "msg={msg}"'], shell=True, stdout=subprocess.PIPE)
        # proc = subprocess.call([f'curl -X POST {self.server} --data "msg=test"'], shell=True)
        # request = requests.post(self.server, data={'msg': msg})
        command = f'curl -X POST {self.base_url} --data "message={msg}"'
        command = shlex.split(command)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()
        if process.returncode == 0:
            print('Send', msg, file=sys.stderr)
        else:
            print('Send error', file=sys.stderr)


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
            "formatter": "base",
            "base_url": "http://localhost:5000/log-entry"
        }
    },
    "loggers": {
        "task_8_logger": {
            "level": "DEBUG",
            "handlers": ["console", "server_pusher"]
        }
    }
}
