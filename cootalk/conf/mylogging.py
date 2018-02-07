#! /usr/bin/python

import os
import logging.config


#standard_format = '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
#                  '[%(levelname)s][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

#id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

standard_format = '[%(levelname)s][%(asctime)s] %(message)s'

logfile_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logfile_name = 'all2.log'

if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

logfile_path = os.path.join(logfile_dir,'log', logfile_name)

LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': logfile_path,
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        #logging.getLogger(__name__)
        '': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


def load_my_logging_cfg():
    logging.config.dictConfig(LOGGING_DIC)
    logger = logging.getLogger(__name__)
    logger.info('It works!')

if __name__ == '__main__':
    load_my_logging_cfg()
