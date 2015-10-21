#!/usr/bin/env python
# -*- coding: utf-8 -*-


class RequestHandler(HttpServlet):
    """ generated source for RequestHandler

    """
    service = IService()
    serialVersionUID = 1L
    serviceResponse = None
    _logger = LoggerFactory.getLogger(<missing>)

    def getServiceResponse(self):
        return self.serviceResponse

    def setServiceResponse(self, serviceResponse):
        self.serviceResponse = self.serviceResponse

    def handleRequest(self, request):
        self._logger.info("Inside Request Handler")
        response = ServiceResponse()
        print "serviceMap"
        self.service = serviceMap[request.getServiceName(])
        self._logger.info("Service name is :" + request.getServiceName())
        self._logger.info("Resourse  name is :" + request.getServiceURL())
        response = self.service.processRequest(request, response)
        return response


