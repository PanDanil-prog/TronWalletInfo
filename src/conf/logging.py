from os import getenv


LOGLEVEL = getenv("LOGLEVEL", "INFO")


LOGGING = {
    "version": 1,

    "formatters": {
        "json": {
            "class": "common.formatters.JSONFormatter",
        },
    },

    "handlers": {
        "base": {
            "class": "logging.StreamHandler",
            "formatter": "json",
            "stream": "ext://sys.stderr"
        }
    },

    "loggers": {
        "base": {
            "handlers": ["base"],
            "level": LOGLEVEL
        }
    }
}
