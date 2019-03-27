import logging
from Infrastracture.GenericPageObjects import *
from Services.ErrorService import ErrorsHandler


class ConfirmationScreen:


    def getConfirmationText(self):
        try:
            element = GenericPO.driver.findElementBy(self, config['CONFIRMATION_SCREEN']['LOCATORS']['CONFIRMATION_TEXT_AREA'],
                                                                 By.XPATH)

            return element.text

        except AttributeError:
            logging.error(ErrorsHandler.CONFIRMATION_MISSING)


    def clickOnDone(self):
        GenericPO.driver.findElementBy(self, config['CONFIRMATION_SCREEN']['LOCATORS']['DONE_BUTTON'],
                                          By.XPATH).click()
        time.sleep(4)
        # remove the sleep


    def getTotalPrice(self):
        price = GenericPO.driver.findElementBy(self, config['CONFIRMATION_SCREEN']['LOCATORS']['TOTAL'],
                                                  By.XPATH).text

        return price
