import time

import pytest
from pytest_testconfig import config
from Infrastracture.Base_Test import BaseTest
from PageObjects.EnterPhoneScreenPO import EnterPhoneScreen
from PageObjects.HomePO import HomePage
from Services.SmsServices import SmsService


class EnterPhoneTests(BaseTest):


    def test_100_wrongSmsCode(self):

        HomePage.clickOnCookiePolicyButton(self)

        HomePage.clickOnConnect(self)

        EnterPhoneScreen.enterValidPhoneNumber(self, phone_number=SmsService.getFirstAvailableNumber(self))

        EnterPhoneScreen.submitPhoneNumber(self)

        EnterPhoneScreen.enterWrongSmsCode(self)

        EnterPhoneScreen.submitSmsCode(self)

        wrong_sms_pop_up = EnterPhoneScreen.getPopup(self)

        assert wrong_sms_pop_up is not None

        popup_text = EnterPhoneScreen.getPopupText(self)

        assert popup_text == config['ENTER_PHONE_PAGE']['TEXTS']['WRONG_SMS_POPUP_TEXT']


    def test_101_resendCode(self):

        HomePage.clickOnCookiePolicyButton(self)

        HomePage.clickOnConnect(self)

        EnterPhoneScreen.enterValidPhoneNumber(self, phone_number=SmsService.getFirstAvailableNumber(self))

        EnterPhoneScreen.submitPhoneNumber(self)

        EnterPhoneScreen.clickOnResendCode(self)

        resend_sms_pop_up = EnterPhoneScreen.getPopup(self)

        assert resend_sms_pop_up is not None

        resend_sms_pop_up_text = EnterPhoneScreen.getPopupText(self)

        assert resend_sms_pop_up_text == config['ENTER_PHONE_PAGE']['TEXTS']['RESEND_CODE_POPUP_TEXT'] + "gal"
