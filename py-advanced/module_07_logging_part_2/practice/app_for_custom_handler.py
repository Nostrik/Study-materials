import logging
import logging.config

from custom_handler_pr import dict_config


logging.config.dictConfig(dict_config)

submodule_logger = logging.getLogger("module_logger.submodule_logger")
submodule_logger.setLevel("DEBUG")


def main():
    submodule_logger.debug("Practice")


if __name__ == '__main__':
    main()
