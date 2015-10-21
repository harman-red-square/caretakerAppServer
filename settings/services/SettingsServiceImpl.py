#!/usr/bin/env python
# -*- coding: utf-8 -*-


class SettingsServiceImpl(SettingsService):
    """ generated source for SettingsServiceImpl

    """
    _logger = LoggerFactory.getLogger(<missing>)
    settingsServiceDao = SettingsServiceDao()
    serviceResponse = ServiceResponse()

    def processRequest(self, serviceRequest, serviceResponse):
        if serviceRequest.getMethod() == CaretakerConstants.METHOD_POST:
            try:
                self._logger.info("Inside SettingsService class")
                self._logger.info("Inside POST Method")
                mapper = ObjectMapper()
                info = ServiceResponse()
                userDetailsDTO = mapper.convertValue(serviceRequest.getPayload(), <missing>)
                if StringUtil.isNull(userDetailsDTO.getSettings().getCallsettings()) and StringUtil.isNull(userDetailsDTO.getSettings().getCallsettings()) and StringUtil.isNull(userDetailsDTO.getSettings().getCallsettings()) and StringUtil.isNull(userDetailsDTO.getSettings().getCallsettings()) and StringUtil.isNull(userDetailsDTO.getSettings().getCallsettings()) and StringUtil.isNull(userDetailsDTO.getSettings().getCallsettings()) and StringUtil.isNull(userDetailsDTO.getSettings().getCallsettings()) and StringUtil.isNull(userDetailsDTO.getSettings().getCallsettings()):
                    info.setErrorMsg("There is nothing to update in Settings.")
                else:
                    info = self.settingsServiceDao.updateSettings(userDetailsDTO.getSettings())
                return info
            except (Exception, ), e:
                self.serviceResponse.setStatusMessage(CaretakerConstants.SERVER_INTERNAL_ERROR_MESSAGE)
                self.serviceResponse.setData("")
                e.printStackTrace()
        return self.serviceResponse


