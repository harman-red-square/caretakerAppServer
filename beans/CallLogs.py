#!/usr/bin/env python
# -*- coding: utf-8 -*-


class CallLogs(object):
    """ generated source for CallLogs

    """
    ID = ""
    number = ""
    serviceId = 0
    type = ""
    date = Date()
    emergency = ""
    voicemail = ""
    duration = ""

    def getID(self):
        return self.ID

    def setID(self, iD):
        self.ID = iD

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


