#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SFPController(object):
    """ generated source for SFPController

    """
    _logger = LoggerFactory.getLogger(<missing>)
    requestHandler = RequestHandler()

    def getRequestHandler(self):
        return self.requestHandler

    def setRequestHandler(self, requestHandler):
        self.requestHandler = self.requestHandler

    def create(self, payload, servletRequest):
        serRequest = WebServiceUtil.getRequest(payload, servletRequest)
        serviceResponse = self.requestHandler.handleRequest(serRequest)
        return serviceResponse

    def delete(self, servletRequest):
        self._logger.info("Inside Controller class")
        self._logger.info("Method name is :" + servletRequest.getMethod())
        self._logger.info("Inside delete Method ")
        self._logger.info("servletRequest.getRequestURI(): Resource:  " + servletRequest.getRequestURI())
        serRequest = WebServiceUtil.getRequest(None, servletRequest)
        serviceResponse = self.requestHandler.handleRequest(serRequest)
        return serviceResponse

    def get(self, servletRequest):
        self._logger.info("Inside Controller class")
        self._logger.info("Method name is :" + servletRequest.getMethod())
        self._logger.info("Inside get Method ")
        serRequest = WebServiceUtil.getRequest(None, servletRequest)
        self._logger.info("servletRequest.getRequestURI(): Resource:  " + servletRequest.getRequestURI())
        serviceResponse = self.requestHandler.handleRequest(serRequest)
        return serviceResponse

    def createUpdate(self, payload, servletRequest):
        self._logger.info("Inside Controller class")
        self._logger.info("Method name is :" + servletRequest.getMethod())
        self._logger.info("Inside get Method ")
        self._logger.info("servletRequest.getRequestURI(): Resource:  " + servletRequest.getRequestURI())
        serRequest = WebServiceUtil.getRequest(payload, servletRequest)
        serviceResponse = self.requestHandler.handleRequest(serRequest)
        return serviceResponse

    def plain(self, request):
        self._logger.info("Inside Controller class")
        self._logger.info("Method name is :" + request.getMethod())
        self._logger.info("Inside get Method ")
        self._logger.info("servletRequest.getRequestURI(): Resource:  " + request.getRequestURI())
        return "ok success"


