import logging


class CustomFileHandlerForHwMod07(logging.Handler):

    def __init__(self, file_name, mode='w'):
        super().__init__()
        self.file = file_name
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        with open(self.file, mode=self.mode) as f:
            f.write(msg + '\n')


dict_config = {
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
        }
    },
    "loggers": {
        "module_calc": {
            "level": "DEBUG",
            "handlers": ["console"],
            # "propagate": False
        }
    },
    "filters": {},
    "root": {}  # == "": {}
}
