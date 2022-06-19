import logging
import subprocess
import sys
import shlex


class SendHandler(logging.Handler):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url

    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record)
        command = f'curl -X POST {self.base_url} --data "message={message}"'
        command = shlex.split(command)
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, )
        process.wait()
        if process.returncode == 0:
            print('Send ', message, file=sys.stderr)
        else:
            print('Send error', file=sys.stderr)


dict_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'base': {
            'format': '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
            'datefmt': '%H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            '()': SendHandler,
            'level': 'DEBUG',
            'formatter': 'base',
            'base_url': 'http://localhost:5000/set_log_info'
        },
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    },
}