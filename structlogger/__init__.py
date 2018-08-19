import collections
import logging
import logging.config
import os
import threading

import structlog
from pythonjsonlogger import jsonlogger

__version__ = "v0.1.3"

try:
    import click

    def _handle_log_level(ctx, param, value):
        level = logging.getLevelName(value.upper())

        if not isinstance(level, int):
            raise click.BadParameter(
                'Must be CRITICAL, ERROR, WARNING, INFO or DEBUG, not "{}"'.format(
                    value
                )
            )

        logging.getLogger().setLevel(level)

    log_level_option = click.option(
        "--log-level",
        callback=_handle_log_level,
        default="INFO",
        is_eager=True,
        expose_value=False,
        help="Desired logging level, must be CRITICAL, ERROR, WARNING, INFO or DEBUG.",
    )
except ImportError:
    pass


def _add_thread_info(logger, method_name, event_dict):
    thread = threading.current_thread()

    event_dict["_thread_name"] = thread.name

    return event_dict


def _order_keys(logger, method_name, event_dict):
    return collections.OrderedDict(
        sorted(event_dict.items(), key=lambda item: (item[0] != "event", item))
    )


def configure_logger(
    log_to_console=True, color_console=True, log_to_file=True, filename=None
):
    pre_chain = [
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        _add_thread_info,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        _order_keys,
    ]

    structlog.configure_once(
        processors=pre_chain
        + [
            structlog.stdlib.filter_by_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        wrapper_class=structlog.stdlib.BoundLogger,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )

    handlers = {}
    if log_to_console:
        handlers["console"] = {"()": logging.StreamHandler, "formatter": "console"}
    if log_to_file and filename:
        handlers["file"] = {
            "()": logging.handlers.RotatingFileHandler,
            "filename": filename,
            "formatter": "json",
            "maxBytes": 25000000,
            "backupCount": 5,
        }

    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.dev.ConsoleRenderer(colors=color_console),
                "foreign_pre_chain": pre_chain,
            },
            "json": {
                "()": structlog.stdlib.ProcessorFormatter,
                "processor": structlog.processors.JSONRenderer(),
                "foreign_pre_chain": pre_chain,
            },
        },
        "handlers": handlers,
        "loggers": {
            "": {"propagate": True, "handlers": list(handlers.keys()), "level": "DEBUG"}
        },
    }
    logging.config.dictConfig(logging_config)
