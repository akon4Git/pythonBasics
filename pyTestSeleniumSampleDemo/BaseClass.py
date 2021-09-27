import inspect
import logging

class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3] # this is to avoid printing the baseclass name file from which the test was invoked
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger


