import logging
from logging.config import dictConfig
from module_07_logging_part_2.homework.task_8_dict_config import d_config


logging.config.dictConfig(d_config)
logger = logging.getLogger('task_8_logger')


def main():
    logger.debug("debug_test")
    logger.info("info_test")
    logger.error("error_test")
    logger.critical("critical_error")
    logger.warning("warning_error")


if __name__ == '__main__':
    main()
