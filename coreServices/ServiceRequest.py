#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ServiceRequest(object):
    """ generated source for ServiceRequest

    """
    serviceName = ""
    serviceURL = ""
    method = ""
    payload = Object()
    servletRequest = HttpServletRequest()
    queryParameter = ""

    def getQueryParameter(self):
        return self.queryParameter

    def setQueryParameter(self, queryParameter):
        self.queryParameter = self.queryParameter

    def getServiceName(self):
        return self.serviceName

    def setServiceName(self, serviceName):
        self.serviceName = self.serviceName

    def getServiceURL(self):
        return self.serviceURL

    def setServiceURL(self, serviceURL):
        self.serviceURL = self.serviceURL

    def getMethod(self):
        return self.method

    def setMethod(self, method):
        self.method = self.method

    def getPayload(self):
        return self.payload

    def setPayload(self, payload):
        self.payload = self.payload

    def getServletRequest(self):
        return self.servletRequest

    def setServletRequest(self, servletRequest):
        self.servletRequest = self.servletRequest


