#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TonesSettingsDTO(object):
    """ generated source for TonesSettingsDTO

    """
    ringtone = TonesDTO()
    alerts = TonesDTO()

    def getRingtone(self):
        return self.ringtone

    def setRingtone(self, ringtone):
        self.ringtone = self.ringtone

    def getAlerts(self):
        return self.alerts

    def setAlerts(self, alerts):
        self.alerts = self.alerts


