#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SoundSettingsDTO(object):
    """ generated source for SoundSettingsDTO

    """
    vibrate = ""
    volume = VolumeDTO()
    tones = TonesSettingsDTO()

    def getVibrate(self):
        return self.vibrate

    def setVibrate(self, vibrate):
        self.vibrate = self.vibrate

    def getVolume(self):
        return self.volume

    def setVolume(self, volume):
        self.volume = self.volume

    def getTones(self):
        return self.tones

    def setTones(self, tones):
        self.tones = self.tones


