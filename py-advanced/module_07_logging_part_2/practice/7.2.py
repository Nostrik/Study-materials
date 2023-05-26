import logging.config
from config_dict_pr import dict_config

logging.config.dictConfig(dict_config)
# root_logger = logging.getLogger()
# module_logger = logging.getLogger('module_logger')
# submodule_logger = logging.getLogger('module_logger.submodule_logger')

# formatter = logging.Formatter(fmt="%(name)s || %(levelname)s || %(message)s || %(module)s.%(funcName)s:%(lineno)d")
# root_logger = logging.getLogger('root_logger')
# root_logger.setLevel('DEBUG')
# root_handler = logging.StreamHandler()
# root_handler.setFormatter(formatter)
# root_logger.addHandler(root_handler)
#
# sub_1 = logging.getLogger('sub_1')
# sub_1.setLevel('INFO')
# sub_1.propagate = True
#
#
# custom_handler = logging.StreamHandler()
# custom_handler.setFormatter(formatter)
#
# sub_1.addHandler(custom_handler)
#
# sub_2 = logging.getLogger('sub_2')
# sub_2.propagate = False
#
# sub_sub_1 = logging.getLogger('sub_2.sub_1')
# sub_sub_1.setLevel('DEBUG')
# sub_sub_1.addHandler(custom_handler)


def main():
    pass


if __name__ == '__main__':
    main()
