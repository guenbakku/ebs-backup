# coding: utf-8

#
# Configuration of app
#

import core.utils as utils

logging = {
    "version": 1,
    "disable_existing_loggers": True, # Disable log from third party library
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "simple",
            "filename": utils.abspath("./logs/log.txt"),
            "maxBytes": 2097152,
            "backupCount": 5,
            "encoding": "utf8"
        },
        'null': {
            'class': 'logging.NullHandler',
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console", "file"],
    },
}
