#!/usr/bin/env python
# -*- coding: utf-8 -*-


class WebServiceUtil(object):
    """ generated source for WebServiceUtil

    """
    requestHandler = RequestHandler()
    _logger = LoggerFactory.getLogger(<missing>)

    @classmethod
    def getServiceNameFromURL(cls, URL):
        start = URL.indexOf("sfp/")
        serviceResourcePart = URL.substring(start + len("sfp/"), len(URL))
        return serviceResourcePart

    @classmethod
    def getServiceResourceFromURL(cls, URL):
        s = URL
        s = s.substring(s.lastIndexOf("/") + 1)
        urlString = StringUtil.encodeURL(s)
        return urlString

    @classmethod
    def formWebServiceReponse(cls, serviceResponse):
        webServiceResponse = WebServiceResponse()
        return webServiceResponse

    @classmethod
    def getRequest(cls, payload, servletRequest):
        methodType = servletRequest.getMethod()
        serviceName = WebServiceUtil.cls.getServiceNameFromURL(servletRequest.getRequestURI())
        serviceURL = WebServiceUtil.cls.getServiceResourceFromURL(servletRequest.getRequestURI())
        queryParameter = servletRequest.getQueryString()
        serRequest = ServiceRequest(serviceName, serviceURL, methodType, payload, servletRequest, queryParameter)
        return serRequest


