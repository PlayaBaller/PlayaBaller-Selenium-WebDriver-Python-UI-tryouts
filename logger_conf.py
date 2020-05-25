import logging
import logging.config


class LoggerConf:
    def logConf(self):
        logging.config.fileConfig('logger.conf')
        logger = logging.getLogger(LoggerConf.__name__)

        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.warning("This is the warning message")
        logger.error("This is an error message")
        logger.critical('This is a critical message')


lg = LoggerConf()
lg.logConf()
