#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StringUtil(object):
    """ generated source for StringUtil

    """

    @classmethod
    def encodeURL(cls, URL):
        urlString = URL.replaceAll("%20", " ")
        print ">>>>>>>>>>>>>>URL Value>>>>>>>>..." + urlString
        return urlString

    @classmethod
    def isNullOrEmpty(cls, dataStr):
        isEmpty = False
        if dataStr is None or dataStr is not None and len((dataStr) == 0) or len((dataStr.trim()) == 0):
            isEmpty = True
        return isEmpty

    @classmethod
    def isNull(cls, obj):
        cls.isNull = False
        if obj is None:
            cls.isNull = True
        return cls.isNull

    @classmethod
    def obj2Str(cls, obj):
        strval = ""
        if obj is not None:
            strval = str(obj)
        return strval


