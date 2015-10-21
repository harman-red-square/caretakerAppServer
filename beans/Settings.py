#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Settings(object):
    """ generated source for Settings

    """
    ID = ""
    callsettings = CallSettings()
    networkConnectSettings = NetworkConnectSettings()
    cellularDataSettings = CellularDataSettings()
    personalization = Personalization()
    privacy = Privacy()
    storage = Storage()
    battery = Battery()
    accessibility = Accessibility()

    def getPersonalization(self):
        return self.personalization

    def setPersonalization(self, personalization):
        self.personalization = self.personalization

    def getPrivacy(self):
        return self.privacy

    def setPrivacy(self, privacy):
        self.privacy = self.privacy

    def getStorage(self):
        return self.storage

    def setStorage(self, storage):
        self.storage = self.storage

    def getBattery(self):
        return self.battery

    def setBattery(self, battery):
        self.battery = self.battery

    def getAccessibility(self):
        return self.accessibility

    def setAccessibility(self, accessibility):
        self.accessibility = self.accessibility

    def getCellularDataSettings(self):
        return self.cellularDataSettings

    def setCellularDataSettings(self, cellularDataSettings):
        self.cellularDataSettings = self.cellularDataSettings

    def getNetworkConnectSettings(self):
        return self.networkConnectSettings

    def setNetworkConnectSettings(self, networkConnectSettings):
        self.networkConnectSettings = self.networkConnectSettings

    def getID(self):
        return self.ID

    def setID(self, iD):
        self.ID = iD

    def getCallsettings(self):
        return self.callsettings

    def setCallsettings(self, callsettings):
        self.callsettings = self.callsettings


