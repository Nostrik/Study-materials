import logging
from typing import Union, Callable
from operator import sub, mul, truediv, add


OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
}

Numeric = Union[int, float]

logger = logging.getLogger('module_utils')
formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s |")
logger.setLevel("DEBUG")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.debug('import utils')


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    if not isinstance(value, str):
        logger.critical(f'wrong operator type, {value}')
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        logger.critical(f'wrong operator value, {value}')
        raise ValueError("wrong operator value")

    return OPERATORS[value]
