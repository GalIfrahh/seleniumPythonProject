from Infrastracture.GenericPageObjects import *


class Checkout:



    def addPaymentFromCheckout(self):
        GenericPO.driver.findElementBy(self, "//div[@class='add-payment-method ng-binding ng-scope']",
                                          By.XPATH)


    def clickOnSubmitOrder(self):
        if GenericPO.driver.waitForInvisibilityOfElem(self, "//div[@class='loading']") is True:
                GenericPO.driver.waitForElemToBeClickable(config['CHECKOUT_SCREEN']['LOCATORS']['SUBMIT_ORDER_BUTTON'])



    def enter4DigitsCode(self):
        GenericPO.driver.findElementBy(self, config['CHECKOUT_SCREEN']['LOCATORS']['ENTER_PIN_INPUT'],
                                    By.XPATH).send_keys(
            config['FORM_PAGE']['DATA']['PIN'])

    def submit4digitsCode(self):
        GenericPO.driver.findElementBy(self, config['CHECKOUT_SCREEN']['LOCATORS']['POPUP_OK_BTN'],
                                          By.XPATH).click()
        time.sleep(2)


    def Pass4DigitsPin(self):
            if config['CHECKOUT_SCREEN']['DATA']['4_DIGIT_EXIST'] == 1:

                Checkout.enter4DigitsCode(self)

                Checkout.submit4digitsCode(self)

            else:
                  pass

    def getErrorPopup(self):
        pop_up_element = GenericPO.driver.waitForVisibilityOfElem(self, config['CHECKOUT_SCREEN']['LOCATORS']['CHECKOUT_POPUP'])

        return pop_up_element


    def clickOnPopUpOkBtn(self):
        GenericPO.driver.findElementBy(self, config['CHECKOUT_SCREEN']['LOCATORS']['POPUP_OK_BTN'], By.XPATH).click()

        time.sleep(1)

    def getErrorPopupText(self):
        text = GenericPO.driver.waitForVisibilityOfElem(self, config['CHECKOUT_SCREEN']['LOCATORS']['CHECKOUT_POPUP']).text

        return text


    def clickOnManagePaymentMethod(self):
        GenericPO.driver.findElementBy(self, config['CHECKOUT_SCREEN']['LOCATORS']['MANAGE_PAYMENT_METHOD'], By.XPATH).click()
