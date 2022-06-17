import logging
from logging.config import dictConfig
from module_07_logging_part_2.homework.task_8_dict_config import d_config


logging.config.dictConfig(d_config)
logger = logging.getLogger('task_8_logger')


def main(cnt):
    if cnt == 0:
        logger.debug("debug_test")
    elif cnt == 1:
        logger.info("info_test")
    elif cnt == 2:
        logger.error("error_test")
    elif cnt == 3:
        logger.critical("critical_error")
    elif cnt == 4:
        logger.warning("warning_error")
    else:
        exit(0)


if __name__ == '__main__':
    # while True:
        # val = int(input(' '))
    main(0)
    main(1)
    main(2)
    main(3)
