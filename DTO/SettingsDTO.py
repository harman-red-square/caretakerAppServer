#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SettingsDTO(object):
    """ generated source for SettingsDTO

    """
    callsettings = CallSettingsDTO()
    networkConnectSettingsDTO = NetworkConnectSettingsDTO()
    cellularDataSettingsDTO = CellularDataSettingsDTO()
    personalizationDTO = PersonalizationDTO()
    privacyDTO = PrivacyDTO()
    storageDTO = StorageDTO()
    batteryDTO = BatteryDTO()
    accessibilityDTO = AccessibilityDTO()

    def getAccessibilityDTO(self):
        return self.accessibilityDTO

    def setAccessibilityDTO(self, accessibilityDTO):
        self.accessibilityDTO = self.accessibilityDTO

    def getBatteryDTO(self):
        return self.batteryDTO

    def setBatteryDTO(self, batteryDTO):
        self.batteryDTO = self.batteryDTO

    def getStorageDTO(self):
        return self.storageDTO

    def setStorageDTO(self, storageDTO):
        self.storageDTO = self.storageDTO

    def getPrivacyDTO(self):
        return self.privacyDTO

    def setPrivacyDTO(self, privacyDTO):
        self.privacyDTO = self.privacyDTO

    def getPersonalizationDTO(self):
        return self.personalizationDTO

    def setPersonalizationDTO(self, personalizationDTO):
        self.personalizationDTO = self.personalizationDTO

    def getCellularDataSettingsDTO(self):
        return self.cellularDataSettingsDTO

    def setCellularDataSettingsDTO(self, cellularDataSettingsDTO):
        self.cellularDataSettingsDTO = self.cellularDataSettingsDTO

    def getNetworkConnectSettingsDTO(self):
        return self.networkConnectSettingsDTO

    def setNetworkConnectSettingsDTO(self, networkConnectSettingsDTO):
        self.networkConnectSettingsDTO = self.networkConnectSettingsDTO

    def getCallsettings(self):
        return self.callsettings

    def setCallsettings(self, callsettings):
        self.callsettings = self.callsettings


