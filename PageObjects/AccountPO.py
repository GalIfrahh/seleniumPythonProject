import logging

from Infrastracture.GenericPageObjects import *
from selenium.common.exceptions import NoSuchElementException

from Services.ErrorService import ErrorsHandler


class Account:




    def clickOnAccountInformation(self):
        GenericPO.driver.hoverAndClick(self, config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                    config['HOME_PAGE']['LOCATORS']['ACCOUNT']['PERSONAL_INFO_BUTTON'])


    def clickOnPaymentMethods(self):
        time.sleep(3)
        # GenericPO.webDriver.waitForVisibilityOfElem(params['HOME_PAGE']['LOCATORS']['ACCOUNT']['PAYMENT_METHODS_BUTTON'])

        try:

                GenericPO.driver.hoverAndClick(self, config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                    config['HOME_PAGE']['LOCATORS']['ACCOUNT']['PAYMENT_METHODS_BUTTON'])
                time.sleep(1)

                wallet_section = GenericPO.driver.waitForVisibilityOfElem(config['WALLET']['LOCATORS']['CARDS_SECTION'])


                if wallet_section is None:

                    GenericPO.driver.hoverAndClick(self, config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                                  config['HOME_PAGE']['LOCATORS']['ACCOUNT']['PAYMENT_METHODS_BUTTON'])
                    time.sleep(1)

        except NoSuchElementException:
                    logging.error(ErrorsHandler.WALLET_IS_NOT_VISIBLE)

    def clickOnGiftCards(self):
        GenericPO.driver.hoverAndClick(self, config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                    config['HOME_PAGE']['LOCATORS']['ACCOUNT']['GIFT_CARDS'])

    def clickOnHistory(self):
        time.sleep(2)
        GenericPO.driver.hoverAndClick(self, config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                    config['HOME_PAGE']['LOCATORS']['ACCOUNT']['HISTORY'])
        time.sleep(2)



    def clickOnLogOut(self):
        GenericPO.driver.hoverAndClick(self, config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                    config['HOME_PAGE']['LOCATORS']['ACCOUNT']['LOG_OUT'])


    def logOutYes(self):
        GenericPO.driver.findElementBy(self, config['LOGOUT_SCREEN']['YES_BTN'], By.XPATH).click()


    def logOutNo(self):
        GenericPO.driver.findElementBy(self, config['LOGOUT_SCREEN']['NO_BTN'], By.XPATH).click()

