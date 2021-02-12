from .levels import LogLevel


class LoggingLayer():

    def __init__(self,logger):
        self.logger=logger

    def log(self,any:object,loglevel:LogLevel=LogLevel.DEBUG)->object:
        LogLevel.selectLoggingMethod(self.logger,loglevel)(str(any))
        return any

