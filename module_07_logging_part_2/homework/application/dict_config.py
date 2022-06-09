import logging


class CustomFileHandlerForHwMod07(logging.Handler):

    def __init__(self, file_1, file_2,  mode='w'):
        super().__init__()
        self.file_1 = file_1
        self.file_2 = file_2
        self.mode = mode

    def emit(self, record: logging.LogRecord) -> None:
        msg = self.format(record)
        if record.levelname == "DEBUG":
            with open(self.file_1, mode=self.mode) as f:
                f.write(msg + '\n')
        elif record.levelname == "INFO":
            with open(self.file_2, mode=self.mode) as f:
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
        },
        "file": {
            "()": CustomFileHandlerForHwMod07,
            "level": "DEBUG",
            "formatter": "base",
            "file_1": "debug_file.log",
            "file_2": "info_file.log",
            "mode": "a"
        }
    },
    "loggers": {
        "module_calc": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            # "propagate": False
        },
        "module_utils": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            # "propagate": True
        }
    },
    "filters": {},
    "root": {}  # == "": {}
}
