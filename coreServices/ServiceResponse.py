#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ServiceResponse(object):
    """ generated source for ServiceResponse

    """
    statusMessage = ""
    errorMsg = ""
    data = Object()

    def getStatusMessage(self):
        return self.statusMessage

    def setStatusMessage(self, statusMessage):
        self.statusMessage = self.statusMessage

    def getErrorMsg(self):
        return self.errorMsg

    def setErrorMsg(self, errorMsg):
        self.errorMsg = self.errorMsg

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = self.data

    def toString(self):
        return "ServiceResponse [statusMessage=" + self.statusMessage + ", errorMsg=" + self.errorMsg + ", data=" + self.data + "]"


