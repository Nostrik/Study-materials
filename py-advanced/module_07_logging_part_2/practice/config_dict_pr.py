
dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(name)s || %(levelname)s || %(message)s || %(module)s.%(funcName)s:%(lineno)d"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },
        "file": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base"
        },

    },
    "loggers": {
        "sub_1": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": True
        },
        "sub_2": {
            "level": {},
            "handlers": ["console", "file"],
            "propagate": False
        },
        "sub_sub_1": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False
        }
    }
}
