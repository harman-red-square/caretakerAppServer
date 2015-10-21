#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PrivacyDTO(object):
    """ generated source for PrivacyDTO

    """
    screenlock = ""
    passCodeLock = PassCodeLockDTO()

    def getScreenlock(self):
        return self.screenlock

    def setScreenlock(self, screenlock):
        self.screenlock = self.screenlock

    def getPassCodeLock(self):
        return self.passCodeLock

    def setPassCodeLock(self, passCodeLock):
        self.passCodeLock = self.passCodeLock


