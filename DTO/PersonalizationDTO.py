#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PersonalizationDTO(object):
    """ generated source for PersonalizationDTO

    """
    soundSettings = SoundSettingsDTO()
    homeScreen = [()
    search = SearchDTO()
    dateTime = DateTimeDTO()
    language = ""

    def getHomeScreen(self):
        return self.homeScreen

    def setHomeScreen(self, homeScreen):
        self.homeScreen = self.homeScreen

    def getSearch(self):
        return self.search

    def setSearch(self, search):
        self.search = self.search

    def getDateTime(self):
        return self.dateTime

    def setDateTime(self, dateTime):
        self.dateTime = self.dateTime

    def getLanguage(self):
        return self.language

    def setLanguage(self, language):
        self.language = self.language

    def getSoundSettings(self):
        return self.soundSettings

    def setSoundSettings(self, soundSettings):
        self.soundSettings = self.soundSettings


