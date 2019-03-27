from Infrastracture.GenericPageObjects import *
from Services.SmsServices import SmsService
from Services.utils import ProjectUtils


class EnterPhoneScreen:



    def getPhoneFieldElement(self):
        element = GenericPO.driver.findElementBy(self, config['ENTER_PHONE_PAGE']['LOCATORS']['PHONE_FIELD'], By.XPATH)
        return element


    def enterValidPhoneNumber(self, phone_number):
        GenericPO.driver.findElementBy(self, config['ENTER_PHONE_PAGE']['LOCATORS']['PHONE_FIELD'], By.XPATH).send_keys\
            (phone_number)


    def submitPhoneNumber(self):
        GenericPO.driver.findElementBy(self, config['ENTER_PHONE_PAGE']['LOCATORS']['SUBMIT_BUTTON'], By.XPATH).click()

        GenericPO.driver.switchToWindow(self, 1)


    def getPopup(self):
        screen_popup = GenericPO.driver.waitForVisibilityOfElem(self,
            config['ENTER_PHONE_PAGE']['LOCATORS']['SCREEN_POPUP'])

        return screen_popup


    def getPopupText(self):
        screen_popup_text = GenericPO.driver.waitForVisibilityOfElem(self,
            config['ENTER_PHONE_PAGE']['LOCATORS']['SCREEN_POPUP_BODY']).text

        return screen_popup_text


    def clickOnPopupOkBtn(self):
        GenericPO.driver.waitForVisibilityOfElem(self,
            config['ENTER_PHONE_PAGE']['LOCATORS']['SCREEN_POPUP_OK']).click


    def enterSmsCode(self):

        code = SmsService.getSmsCode(self)

        GenericPO.driver.switchToWindow(self, 0)

        time.sleep(1)

        GenericPO.driver.findElementBy(self, config['ENTER_PHONE_PAGE']['LOCATORS']['ENTER_SMS_CODE'],
                                    By.XPATH).send_keys(code)

        # code = ApiHelper.getCode(phoneToken)
        # code = raw_input()


    def enterWrongSmsCode(self):

        GenericPO.driver.switchToWindow(self, 0)

        rand_sms_code = ProjectUtils.createRandomSmsCode()

        GenericPO.driver.waitForVisibilityOfElem(self, config['ENTER_PHONE_PAGE']['LOCATORS']['ENTER_SMS_CODE']).\
            send_keys(rand_sms_code)


    def submitSmsCode(self):
        GenericPO.driver.findElementBy(self, config['ENTER_PHONE_PAGE']['LOCATORS']['SUBMIT_SMS_CODE'],
                                By.XPATH).click()

        GenericPO.driver.waitForVisibilityOfElem(self, config['HOME_PAGE']['LOCATORS']['CONNECT_BTN_TEXT_AREA'])

        #time.sleep(3)

    def clickOnResendCode(self):

        GenericPO.driver.switchToWindow(self, 0)

        GenericPO.driver.findElementBy(self, config['ENTER_PHONE_PAGE']['LOCATORS']['RESEND_CODE'],
                                          By.XPATH).click()
