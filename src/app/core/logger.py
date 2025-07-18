import os
import logging

from pythonjsonlogger import jsonlogger

from .settings import settings


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"

def setup_logger(name: str) -> logging.Logger:
    """ Setup configuration of the root logger of the application """

    # get instance of root logger
    logger = logging.getLogger(__name__)
    formatter = jsonlogger.JsonFormatter()

    # configure formatter for logger
    formatter = logging.Formatter(LOG_FORMAT)

    # configure console handler
    console = logging.StreamHandler()
    console.setFormatter(formatter)

    # configure rotating file handler
    file = logging.handlers.RotatingFileHandler(
                filename=os.path.join(
                    settings.LOG_DIRECTORY,
                    "app.log",
                ),
                mode="a",
                # Creates a new file every 15MB
                maxBytes=15000000, # 15MB
                backupCount=5,
            )
    file.setFormatter(formatter)

    # add handlers
    logger.addHandler(console)
    logger.addHandler(file)

    # configure logger level
    logger.setLevel(settings.LOG_LEVEL)

    return logger
