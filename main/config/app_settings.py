#coding=utf-8
__author__ = 'wanglu'

STATIC_URL="/static"

SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:root@localhost:3306/test?charset=utf8mb4"

APPID = "***"
APPSECRET = "***"

APP_TOKEN = "***"


#日志配置
formatter = '[%(asctime)s][%(filename)s:%(lineno)s][%(levelname)s][%(message)s]'

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,  # this fixes the problem

    'formatters': {
        'standard': {
            'format': formatter,
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        "debug_file_handler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "standard",
            "filename": "logs/debug.log",
            "when": "D",
            "interval": 1,
            #"maxBytes": 1048576000,
            "backupCount": 30,
            "encoding": "utf8"
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'debug_file_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
        'requests': {
            'handlers': ['default', 'debug_file_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'flask':{
            'handlers': ['default', 'debug_file_handler'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}
