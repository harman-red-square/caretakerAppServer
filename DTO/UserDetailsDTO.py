#!/usr/bin/env python
# -*- coding: utf-8 -*-


class UserDetailsDTO(object):
    """ generated source for UserDetailsDTO

    """
    userId = ""
    settings = SettingsDTO()

    def getSettings(self):
        return self.settings

    def setSettings(self, settings):
        self.settings = self.settings

    def getUserId(self):
        return self.userId

    def setUserId(self, userId):
        self.userId = self.userId


