#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SFPLogger(object):
    """ generated source for SFPLogger

    """
    _logger = LoggerFactory.getLogger(<missing>)

    @classmethod
    def handleUninitializedLogger(cls):
        cls._logger.cls.error("Uninitialized logger passed by application for logging", Throwable())

    @classmethod
    @overloaded
    def error(cls, logger, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.error("Msg={}", msg)

    @classmethod
    @error.register(type, Logger, str, Exception)
    def error_0(cls, logger, msg, e):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.error("Msg=" + msg, e)

    @classmethod
    @error.register(type, Logger, str, str)
    def error_1(cls, logger, transactionId, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.error("TRANSID:{}, Msg={}", "")

    @classmethod
    @error.register(type, Logger, str, str, Exception)
    def error_2(cls, logger, transactionId, msg, e):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.error("TRANSID:" + transactionId + ", Msg=" + msg, e)

    @classmethod
    @error.register(type, Logger, str, str, str)
    def error_3(cls, logger, transactionId, user, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.error("TRANSID:{}, User:{}, Msg={}", "")

    @classmethod
    @error.register(type, Logger, str, str, str, Exception)
    def error_4(cls, logger,
                     transactionId,
                     user,
                     msg,
                     e):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.error("TRANSID:" + transactionId + ", User:" + user + ", Msg=" + msg, e)

    @classmethod
    @overloaded
    def debug(cls, logger, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.debug("Msg={}", msg)

    @classmethod
    @debug.register(type, Logger, str, str)
    def debug_0(cls, logger, transactionId, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.debug("TRANSID:{}, Msg={}", "")

    @classmethod
    @debug.register(type, Logger, str, str, str)
    def debug_1(cls, logger, transactionId, user, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.debug("TRANSID:{}, User:{}, Msg={}", "")

    @classmethod
    @overloaded
    def info(cls, logger, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.info("Msg={}", msg)

    @classmethod
    @info.register(type, Logger, str, str)
    def info_0(cls, logger, transactionId, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.info("TRANSID:{}, Msg={}", "")

    @classmethod
    @info.register(type, Logger, str, str, str)
    def info_1(cls, logger, transactionId, user, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.info("TRANSID:{}, User:{}, Msg={}", "")

    @classmethod
    @overloaded
    def warn(cls, logger, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.warn("Msg={}", msg)

    @classmethod
    @warn.register(type, Logger, str, str)
    def warn_0(cls, logger, transactionId, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.warn("TRANSID:{}, Msg={}", "")

    @classmethod
    @warn.register(type, Logger, str, str, str)
    def warn_1(cls, logger, transactionId, user, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.warn("TRANSID:{}, User:{}, Msg={}", "")

    @classmethod
    @overloaded
    def trace(cls, logger, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.trace("Msg={}", msg)

    @classmethod
    @trace.register(type, Logger, str, str)
    def trace_0(cls, logger, transactionId, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.trace("TRANSID:{}, Msg={}", "")

    @classmethod
    @trace.register(type, Logger, str, str, str)
    def trace_1(cls, logger, transactionId, user, msg):
        if logger is None:
            cls.handleUninitializedLogger()
        else:
            logger.cls.trace("TRANSID:{}, User:{}, Msg={}", "")

    @classmethod
    def stopLoggerContext(cls):
        loggerContext = LoggerFactory.getILoggerFactory()
        loggerContext.stop()


