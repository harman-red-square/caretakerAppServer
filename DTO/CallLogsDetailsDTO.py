#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CallLogsDetailsDTO(object):
    """ generated source for CallLogsDetailsDTO

    """
    userId = ""
    number = ""
    serviceId = 0
    type = ""
    date = Date()
    emergency = ""
    voicemail = ""
    duration = ""

    def getUserId(self):
        return self.userId

    def setUserId(self, userId):
        self.userId = self.userId

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = self.number

    def getServiceId(self):
        return self.serviceId

    def setServiceId(self, serviceId):
        self.serviceId = self.serviceId

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = self.type

    def getDate(self):
        return self.date

    def setDate(self, date):
        self.date = self.date

    def getEmergency(self):
        return self.emergency

    def setEmergency(self, emergency):
        self.emergency = self.emergency

    def getVoicemail(self):
        return self.voicemail

    def setVoicemail(self, voicemail):
        self.voicemail = self.voicemail

    def getDuration(self):
        return self.duration

    def setDuration(self, duration):
        self.duration = self.duration


