from Infrastracture.GenericPageObjects import *
from PageObjects.AccountPO import Account
from PageObjects.EnterEmailScreenPO import EnterEmailPage
from PageObjects.EnterPhoneScreenPO import EnterPhoneScreen
from PageObjects.FormScreenPO import FormPage
from PageObjects.HomePO import HomePage
from Services.SmsServices import SmsService


class Connect:

    def login(self):

        HomePage.clickOnCookiePolicyButton(self)

        HomePage.clickOnConnect(self)

        EnterPhoneScreen.enterValidPhoneNumber(self, phone_number=SmsService.getFirstAvailableNumber(self))

        EnterPhoneScreen.submitPhoneNumber(self)

        EnterPhoneScreen.enterSmsCode(self)

        EnterPhoneScreen.submitSmsCode(self)

    def register(self):

        Connect.login(self)

        EnterEmailPage.enterUnExistEmail(self)

        EnterEmailPage.submitEmail(self)

        FormPage.enterFullName(self)

        FormPage.enterPin(self)

        FormPage.enterDate(self)

        FormPage.chooseOptinTrue(self)

        FormPage.submitForm(self)


    def logout(self):

        Account.clickOnLogOut(self)

        Account.logOutYes(self)
