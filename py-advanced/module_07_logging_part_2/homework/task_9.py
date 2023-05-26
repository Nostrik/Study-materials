dict_python_conf = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "stdout": {
            "format": "%(asctime)s: (%(levelname)s) %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%Z",
        },
        "applog": {
            "format": "%(asctime)s.%(msecs)d %(process)s %(levelname)s %(message)s",
            "datefmt": "%Y-%m-%dT%H:%M:%S%Z",
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "formatter": "stdout",
            "stream": "ext://sys.stdout"
        },
        "applog": {
            "class": "logging.StreamHandler",
            "formatter": "applog",
            "stream": "ext://sys.stdout"
        }
    },
    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": ["applog"]
        },
        "app": {
            "level": "DEBUG",
            "handlers": ["applog"]
        }
    }
}
