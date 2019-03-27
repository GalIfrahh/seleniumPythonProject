import logging
from Infrastracture.GenericPageObjects import *
from selenium.common.exceptions import NoSuchElementException
from Services.ErrorService import ErrorsHandler


class Account:
    

    def clickOnAccountInformation(self):
        GenericPO.driver.hoverAndClick(self, config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                    config['HOME_PAGE']['LOCATORS']['ACCOUNT']['PERSONAL_INFO_BUTTON'])


        
    def clickOnPaymentMethods(self):
       
       GenericPO.driver.hoverAndClick(self, config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                     config['HOME_PAGE']['LOCATORS']['ACCOUNT']['PAYMENT_METHODS_BUTTON'])
       
    

    def clickOnGiftCards(self):
        GenericPO.driver.hoverAndClick(self, config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                    config['HOME_PAGE']['LOCATORS']['ACCOUNT']['GIFT_CARDS'])

        
    def clickOnHistory(self):
        
        GenericPO.driver.hoverAndClick(self, config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                    config['HOME_PAGE']['LOCATORS']['ACCOUNT']['HISTORY'])



    def clickOnLogOut(self):
        
        GenericPO.driver.hoverAndClick(self, config['HOME_PAGE']['LOCATORS']['ACCOUNT']['ACCOUNT_BUTTON'],
                                    config['HOME_PAGE']['LOCATORS']['ACCOUNT']['LOG_OUT'])


    def logOutYes(self):
        
        GenericPO.driver.findElementBy(self, config['LOGOUT_SCREEN']['YES_BTN'], By.XPATH).click()


    def logOutNo(self):
       
        GenericPO.driver.findElementBy(self, config['LOGOUT_SCREEN']['NO_BTN'], By.XPATH).click()

