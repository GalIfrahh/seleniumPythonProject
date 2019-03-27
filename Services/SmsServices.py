from Infrastracture.GenericPageObjects import *


SMS_PROVIDER_SITE = "http://receive-smss.com/"
PHONE_NUMBER_LOCATOR = "//*[@id='content']/div[1]/div/div/div/div[1]/div[2]/div/h4"
PHONE_NUMBER_BUTTON = "//*[@id='content']/div[1]/div/div/div/div[1]/div[3]/div/a"
SMS_TEXT_LOCATOR_LIST = "//*[@id='content']/div/div/div/div/div/div/div/div/table/tbody/tr/td[2]"


class SmsService(GenericPO):


    def __init__(self):
        pass


    def getFirstAvailableNumber(self):

        GenericPO.driver.executeScript(self, "window.open('');")

        GenericPO.driver.switchToWindow(self, 1)

        GenericPO.driver.openSut(self, SMS_PROVIDER_SITE)

        phone_number = GenericPO.driver.findElementBy(self, PHONE_NUMBER_LOCATOR, By.XPATH).text

        GenericPO.driver.switchToWindow(self, 0)

        return phone_number


    def getSmsCode(self):

        time.sleep(3)

        GenericPO.driver.findElementBy(self, PHONE_NUMBER_BUTTON, By.XPATH).click()

        received_sms_list = self.driver.find_elements_by_xpath(SMS_TEXT_LOCATOR_LIST)

        received_sms_text = received_sms_list[0].text

        sms_code = received_sms_text[received_sms_text.index(": ") + 2:received_sms_text.index(" t")]

        GenericPO.driver.switchToWindow(self, 0)

        return sms_code



