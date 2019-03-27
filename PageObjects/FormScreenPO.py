from Infrastracture.GenericPageObjects import *


class FormPage:



    def enterFullName(self):
        GenericPO.driver.findElementBy(self, config['FORM_PAGE']['LOCATORS']['FORM_FULL_NAME_FIELD'],
                                    By.XPATH).send_keys(
            config['FORM_PAGE']['DATA']['NAME'])


    def enterPin(self):
        GenericPO.driver.findElementBy(self, config['FORM_PAGE']['LOCATORS']['FORM_PIN_FIELD'],
                                    By.XPATH).send_keys(
            config['FORM_PAGE']['DATA']['PIN'])


    def enterDate(self):
        GenericPO.driver.findElementBy(self, config['FORM_PAGE']['LOCATORS']['FORM_DATE_FIELD'],
                                    By.XPATH).send_keys(
            config['FORM_PAGE']['DATA']['DATE'])


    def chooseOptinTrue(self):
        GenericPO.driver.findElementBy(self, config['FORM_PAGE']['LOCATORS']['FORM_OPTIN_TRUE'],
                                    By.XPATH).click()


    def submitForm(self):
        GenericPO.driver.findElementBy(self, config['FORM_PAGE']['LOCATORS']['FORM_SUBMIT_BUTTON'],
                                    By.XPATH).click()

        GenericPO.driver.waitForVisibilityOfElem(self, config['HOME_PAGE']['LOCATORS']['CONNECT_BTN_TEXT_AREA'])
        # time.sleep(3)
