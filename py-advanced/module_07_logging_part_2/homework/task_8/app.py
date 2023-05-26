import logging.config

from send_handler import dict_config

logging.config.dictConfig(dict_config)
app_logger = logging.getLogger('app_logger')


def main():
    app_logger.debug('Hello debug!')
    app_logger.info('Hello info!')
    app_logger.warning('Hello warning!')
    app_logger.exception('Hello exception!')


if __name__ == '__main__':
    main()
