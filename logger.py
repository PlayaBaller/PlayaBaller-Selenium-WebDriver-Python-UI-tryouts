import logging


class LoggerConsole:
    def testLog(self):
        #    creating logger
        logger = logging.getLogger(LoggerConsole.__name__)
        logger.setLevel(logging.DEBUG)

        #   creating console handler and setting level to 'Info'
        chandler = logging.StreamHandler()
        chandler.setLevel(logging.DEBUG)

        #   creating a formatter       time    value defined in logger obj  level of the log msg  message   time format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        #   adding formatter to the console handler, which is chandler
        chandler.setFormatter(formatter)

        #   adding console handler to the logger
        logger.addHandler(chandler)

        # logging messages themselves are
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')


demoobj = LoggerConsole()
demoobj.testLog()
