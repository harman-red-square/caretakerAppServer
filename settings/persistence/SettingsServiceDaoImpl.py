#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SettingsServiceDaoImpl(SettingsServiceDao):
    """ generated source for SettingsServiceDaoImpl

    """
    sessionFactory_ = SessionFactory()
    _logger = LoggerFactory.getLogger(<missing>)
    serviceResponse = ServiceResponse()
    mongo = MongoOperations()

    def updateSettings(self, settingsDTO):
        self.serviceResponse = ServiceResponse()
        self._logger.info("Inside CallLogServiceDaoImpl class")
        self._logger.info("Inside addCallLogs Method")
        try:
            userDetails = UserDetails()
            settings = Settings()
            if not StringUtil.isNull(settingsDTO.getCallsettings()):
                callSettings = self.updateCallSettings(settingsDTO.getCallsettings())
                settings.setCallsettings(callSettings)
            if not StringUtil.isNull(settingsDTO.getNetworkConnectSettingsDTO()):
                networkConnectSettings = self.updateNetworkConnectSettings(settingsDTO.getNetworkConnectSettingsDTO())
                settings.setNetworkConnectSettings(networkConnectSettings)
            if not StringUtil.isNull(settingsDTO.getCellularDataSettingsDTO()):
                cellularDataSettings = self.updateCellularDataSettings(settingsDTO.getCellularDataSettingsDTO())
                settings.setCellularDataSettings(cellularDataSettings)
            if not StringUtil.isNull(settingsDTO.getPersonalizationDTO()):
                personalizationSettings = self.updatePersonalizationSettings(settingsDTO.getPersonalizationDTO())
                settings.setPersonalization(personalizationSettings)
            if not StringUtil.isNull(settingsDTO.getPrivacyDTO()):
                privacySettings = self.updatePrivacySettings(settingsDTO.getPrivacyDTO())
                settings.setPrivacy(privacySettings)
            if not StringUtil.isNull(settingsDTO.getStorageDTO()):
                storageSettings = self.updateStorageSettings(settingsDTO.getStorageDTO())
                settings.setStorage(storageSettings)
            if not StringUtil.isNull(settingsDTO.getBatteryDTO()):
                batterySettings = self.updateBatterySettings(settingsDTO.getBatteryDTO())
                settings.setBattery(batterySettings)
            if not StringUtil.isNull(settingsDTO.getBatteryDTO()):
                accessibilitySettings = self.updateAccessibilitySettings(settingsDTO.getAccessibilityDTO())
                settings.setAccessibility(accessibilitySettings)
            userDetails.setSettings(settings)
            self.mongo.save(userDetails)
            self.serviceResponse.setStatusMessage(CaretakerConstants.SUCCESS_MESSAGE)
        except (HibernateException, ), e:
            self.serviceResponse.setStatusMessage(CaretakerConstants.SERVER_INTERNAL_ERROR_MESSAGE)
        return self.serviceResponse

    def updateCallSettings(self, callSettingsDTO):
        self._logger.info("Inside CallLogServiceDaoImpl class")
        self._logger.info("Inside addCallLogs Method")
        callSettings = CallSettings()
        if not StringUtil.isNullOrEmpty(callSettingsDTO.getVoiceMailNumber()):
            callSettings.setVoiceMailNumber(callSettingsDTO.getVoiceMailNumber())
        if not StringUtil.isNull(callSettingsDTO.getCallForwardDetails()):
            callForward = None
            itr = callSettingsDTO.getCallForwardDetails().iterator()
            while itr.hasNext():
                callForwardDetails = itr.next()
                callForward = CallForward()
                callForward.setIsEnabled(callForwardDetails.getIsEnabled())
                callForward.setNumber(callForwardDetails.getNumber())
                callForward.setType(callForwardDetails.getType())
                callLogsDetailsCollection.add(callForward)
            callSettings.setCallForwardDetails(callLogsDetailsCollection)
        return callSettings

    def updateNetworkConnectSettings(self, networkConnectSettingsDTO):
        self._logger.info("Inside CallLogServiceDaoImpl class")
        self._logger.info("Inside addCallLogs Method")
        networkConnectSettings = NetworkConnectSettings()
        networkConnectSettings.setGeoLocation(networkConnectSettingsDTO.getGeoLocation())
        return networkConnectSettings

    def updateCellularDataSettings(self, cellularDataSettingsDTO):
        self._logger.info("Inside CallLogServiceDaoImpl class")
        self._logger.info("Inside addCallLogs Method")
        cellularDataSettings = CellularDataSettings()
        cellularDataSettings.setDataRoaming(cellularDataSettingsDTO.getDataRoaming())
        return cellularDataSettings

    def updatePersonalizationSettings(self, personalizationDTO):
        self._logger.info("Inside CallLogServiceDaoImpl class")
        self._logger.info("Inside addCallLogs Method")
        personalization = Personalization()
        if not StringUtil.isNull(personalizationDTO.getSoundSettings()):
            soundSettings = SoundSettings()
            volume = Volume()
            tonesSettings = TonesSettings()
            if not StringUtil.isNull(personalizationDTO.getSoundSettings().getVibrate()):
                soundSettings.setVibrate(personalizationDTO.getSoundSettings().getVibrate())
            if not StringUtil.isNull(personalizationDTO.getSoundSettings().getVolume()):
                volume.setAlarm(personalizationDTO.getSoundSettings().getVolume().getAlarm())
                volume.setMedia(personalizationDTO.getSoundSettings().getVolume().getMedia())
                volume.setRingtone(personalizationDTO.getSoundSettings().getVolume().getRingtone())
            soundSettings.setVolume(volume)
            if not StringUtil.isNull(personalizationDTO.getSoundSettings().getTones()):
                tones = Tones()
                if not StringUtil.isNull(personalizationDTO.getSoundSettings().getTones().getRingtone()):
                    tones.setByDefault(personalizationDTO.getSoundSettings().getTones().getRingtone().getByDefault())
                    tones.setRingtone(personalizationDTO.getSoundSettings().getTones().getRingtone().getRingtone())
                    tonesSettings.setRingtone(tones)
                if not StringUtil.isNull(personalizationDTO.getSoundSettings().getTones().getAlerts()):
                    tones.setByDefault(personalizationDTO.getSoundSettings().getTones().getAlerts().getByDefault())
                    tones.setRingtone(personalizationDTO.getSoundSettings().getTones().getAlerts().getRingtone())
                    tonesSettings.setAlerts(tones)
                soundSettings.setTones(tonesSettings)
            personalization.setSoundSettings(soundSettings)
        if not StringUtil.isNull(personalizationDTO.getHomeScreen()):
            personalization.setHomeScreen(personalizationDTO.getHomeScreen())
        if not StringUtil.isNull(personalizationDTO.getSearch()):
            search = Search()
            search.setSearchEngine(personalizationDTO.getSearch().getSearchEngine())
            search.setSearchSuggestions(personalizationDTO.getSearch().getSearchSuggestions())
            personalization.setSearch(search)
        if not StringUtil.isNull(personalizationDTO.getLanguage()):
            personalization.setLanguage(personalizationDTO.getLanguage())
        if not StringUtil.isNull(personalizationDTO.getDateTime()):
            dateTime = DateTime()
            dateTime.setDate(personalizationDTO.getDateTime().getDate())
            dateTime.setSetAutomatically(personalizationDTO.getDateTime().getSetAutomatically())
            dateTime.setTimeFormat(personalizationDTO.getDateTime().getTimeFormat())
            dateTime.setTimeZone(personalizationDTO.getDateTime().getTimeZone())
            personalization.setDateTime(dateTime)
        return personalization

    def updatePrivacySettings(self, privacyDTO):
        self._logger.info("Inside CallLogServiceDaoImpl class")
        self._logger.info("Inside addCallLogs Method")
        privacy = Privacy()
        if not StringUtil.isNull(privacyDTO.getScreenlock()):
            privacy.setScreenlock(privacyDTO.getScreenlock())
        if not StringUtil.isNull(privacyDTO.getPassCodeLock()):
            passCodeLock = PassCodeLock()
            passCodeLock.setIsEnabled(privacyDTO.getPassCodeLock().getIsEnabled())
            passCodeLock.setPasscode(privacyDTO.getPassCodeLock().getPasscode())
            passCodeLock.setRequirePasscode(privacyDTO.getPassCodeLock().getRequirePasscode())
            privacy.setPassCodeLock(passCodeLock)
        return privacy

    def updateStorageSettings(self, storageDTO):
        self._logger.info("Inside CallLogServiceDaoImpl class")
        self._logger.info("Inside addCallLogs Method")
        storage = Storage()
        if not StringUtil.isNull(storageDTO.getMediaStorage()):
            mediaStorage = MediaStorage()
            mediaStorage.setFormat(storageDTO.getMediaStorage().getFormat())
            storage.setMediaStorage(mediaStorage)
        return storage

    def updateBatterySettings(self, batteryDTO):
        self._logger.info("Inside CallLogServiceDaoImpl class")
        self._logger.info("Inside addCallLogs Method")
        battery = Battery()
        battery.setPowerSaverMode(batteryDTO.getPowerSaverMode())
        battery.setTurnAutomatically(battery.getTurnAutomatically())
        return battery

    def updateAccessibilitySettings(self, accessibilityDTO):
        self._logger.info("Inside CallLogServiceDaoImpl class")
        self._logger.info("Inside addCallLogs Method")
        accessibility = Accessibility()
        if not StringUtil.isNull(accessibilityDTO.getColorFilter()):
            colorFilter = ColorFilter()
            colorFilter.setContrast(accessibilityDTO.getColorFilter().getContrast())
            colorFilter.setIsEnabled(accessibilityDTO.getColorFilter().getIsEnabled())
            colorFilter.setGrayscale(accessibilityDTO.getColorFilter().getGrayscale())
            colorFilter.setInvert(accessibilityDTO.getColorFilter().getInvert())
            accessibility.setColorFilter(colorFilter)
        return accessibility


