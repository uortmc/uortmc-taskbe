from enum import IntEnum


class LogLevel(IntEnum):
    DEBUG=1
    ERROR=2

    @staticmethod
    def selectLoggingMethod(logger,level):
        asc={
            LogLevel.DEBUG:logger.debug,
            LogLevel.ERROR:logger.error
        }
        return asc.get(level,logger.debug)

