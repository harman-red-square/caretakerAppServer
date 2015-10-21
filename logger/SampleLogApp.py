#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SampleLogApp(object):
    """ generated source for SampleLogApp

    """
    _logger = LoggerFactory.getLogger(<missing>)

    @classmethod
    def main(cls, args):
        cls.callError()
        cls.callDebug()
        cls.callInfo()
        cls.callWarn()
        cls.callTrace()
        cls.stopLoggerContext()

    @classmethod
    def callError(cls):
        SFPLogger.error(cls._logger, "ERROR")
        SFPLogger.error(cls._logger, "my error debug message", Exception("my exception"))
        SFPLogger.error(cls._logger, "Trans03", "Something wrong with your Transaction...")
        SFPLogger.error(cls._logger, "Trans04", "Something ERROR in your Transaction...", Exception("ERROR"))
        SFPLogger.error(cls._logger, "Trans05", "Harman", "Sorry your Transaction is not processed!!!")
        SFPLogger.error(cls._logger, "Something ERROR found while your Transaction")

    @classmethod
    def callInfo(cls):
        SFPLogger.info(cls._logger, "Message......")
        SFPLogger.info(cls._logger, "Welcome to Logger...")
        SFPLogger.info(cls._logger, "Trans01", "Transaction Sucessfull")
        SFPLogger.info(cls._logger, "Trans02", "Simphony Teleca", "Your Transaction is Completed..")

    @classmethod
    def callDebug(cls):
        SFPLogger.debug(cls._logger, "You are under Debuging Mode Please Wait")
        SFPLogger.debug(cls._logger, "Trans01", "Your Transaction is Under Process")
        SFPLogger.debug(cls._logger, "Trns0014", "SimphonyTeleca", "Please Wait while your Transaction..")

    @classmethod
    def callWarn(cls):
        SFPLogger.warn(cls._logger, "Warning!!!")
        SFPLogger.warn(cls._logger, "Trans001", "Warning!!!  Before Submit verify your Information.")
        SFPLogger.warn(cls._logger, "TR0075", "SimphonyTeleca", "Warning!!!  Before submit verify your Transaction")

    @classmethod
    def callTrace(cls):
        SFPLogger.trace(cls._logger, "Tace your information")
        SFPLogger.trace(cls._logger, "TR12540", "Trace your Transaction....")
        SFPLogger.trace(cls._logger, "TR11541", "Harman", "Trace your Information according to your user name")

    @classmethod
    def stopLoggerContext(cls):
        SFPLogger.cls.stopLoggerContext()

if __name__ == '__main__':
    import sys
    SampleLogApp.main(sys.argv)

