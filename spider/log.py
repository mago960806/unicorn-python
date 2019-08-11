import os
import logging.config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR, 'log')


def get_logger(logger_name: str):
    config = {
        'version': 1,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'main': {
                'datefmt': '%Y-%m-%d %H:%M:%S',
                'format': '%(asctime)s [%(module)s %(levelname)s] %(message)s',
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
                'formatter': 'main'
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOG_DIR, 'spider.log'),
                'level': 'DEBUG',
                'formatter': 'main'
            },
        },
        'loggers': {
            'StreamLogger': {
                'handlers': ['console'],
                'level': 'DEBUG',
            },
            'FileLogger': {
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
            },

        }
    }

    logging.config.dictConfig(config)
    return logging.getLogger(logger_name)


if __name__ == '__main__':
    logger = get_logger('FileLogger')
    logger.info('测试消息')
