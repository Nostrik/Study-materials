import sys
import logging
import logging.config
from utils import string_to_operator
from dict_config import dict_config


logging.config.dictConfig(dict_config)
logger = logging.getLogger('module_calc')
# formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s |")
# logger.setLevel("DEBUG")
# handler = logging.StreamHandler()
# handler.setFormatter(formatter)
# logger.addHandler(handler)
logger.info('start app')


def calc(args):
    logger.debug(f"Arguments: {args}")

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        logger.exception(e)
    try:
        num_2 = float(num_2)
    except ValueError as e:
        logger.exception(e)

    try:
        operator_func = string_to_operator(operator)
        result = operator_func(num_1, num_2)
        logger.debug(f'Result: {result}')
        logger.debug(f'{num_1} {operator} {num_2} = {result}')
    except ValueError as e:
        logger.exception(e)


if __name__ == '__main__':
    calc(sys.argv[1:])
