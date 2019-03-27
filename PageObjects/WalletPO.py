from selenium.common.exceptions import StaleElementReferenceException, WebDriverException
from Infrastracture.GenericPageObjects import *
from PageObjects.AccountPO import Account


class Wallet:



    def clickOnAddNewCard(self):
        if len(Wallet.getUserCardsList()) >= 1 and Wallet.getUserCardsList()[0].text == config['WALLET']['TEXTS']['ADD_NEW_CARD_TEXT']:

                    GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON'],
                                          By.XPATH).click()

        if config['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'] != 0 and Wallet.getUserCardsList()[0].text \
                != config['WALLET']['TEXTS']['ADD_NEW_CARD_TEXT']:

                    GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['ADD_NEW_CARD_BUTTON_HEADER'],
                                          By.XPATH).click()

        # GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
        #                                  (params['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

    def getWalletHeader(self):
        wallet_header = GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['WALLET_HEADER'],
                                          By.XPATH).text
        return wallet_header


    def enterCcNumber(self):
        try:
            GenericPO.driver.switchToIframe(self, GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
                                            (config['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

            GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['CC_NUMBER_INPUT'],
                                          By.ID).send_keys(
                config['WALLET']['DATA']['FIRST_CARD_DETAILS']['VALID_CC_NUMBER'])

        except StaleElementReferenceException:
            print('stale element')

    def enterExpDate(self):
        GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['EXP_DATE_INPUT'],
                                    By.ID).send_keys(config['WALLET']['DATA']['FIRST_CARD_DETAILS']['EXP_DATE'])

    def enterCvc(self):
        GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['CVC_INPUT'],
                                    By.ID).send_keys(config['WALLET']['DATA']['FIRST_CARD_DETAILS']['CVC'])


    def enterPostalCode(self):
        GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['POSTCODE_INPUT'],
                                    By.ID).send_keys(config['WALLET']['DATA']['FIRST_CARD_DETAILS']['POSTCODE'])

    def clickOnCcApplyButton(self):
        GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['APPLY_BUTTON'],
                                    By.ID).click()
        GenericPO.driver.remoteWebDriver.switch_to.default_content(self)

        time.sleep(6)


    def getCcApplyButtonText(self):
        GenericPO.driver.switchToIframe(self, GenericPO.driver.remoteWebDriver.find_element_by_xpath
                                           (config['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

        apply_button_text = GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['APPLY_BUTTON'],
                                    By.ID).text
        return apply_button_text


    def clickOnCcCancelButton(self):


        try:
            GenericPO.driver.switchToIframe(self, GenericPO.driver.remoteWebDriver.find_element_by_xpath
                                               (config['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

            GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['CANCEL_BUTTON'],
                                    By.ID).click()
            GenericPO.driver.remoteWebDriver.switch_to.default_content(self)

        except WebDriverException:
            return False


    def getCcCancelButtonText(self):
        # GenericPO.webDriver.switchToIframe(GenericPO.webDriver.remoteWebDriver.find_element_by_xpath
        #                                  (params['WALLET']['LOCATORS']['CC_VALUES_IFRAME']))

        cancel_button_text = GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['CANCEL_BUTTON'],
                                    By.ID).text
        return cancel_button_text


    def getUserCardsList(self):

        card_list_element = GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['CARDS_SECTION'],
                                    By.XPATH)

        cards = card_list_element.find_elements_by_tag_name(self, config['WALLET']['LOCATORS']['USER_CARDS'])

        return cards


    def getUserCardsNumber(self):

        card_list_element = GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['CARDS_SECTION'],
                                   By.XPATH)

        cards = card_list_element.find_elements_by_tag_name(self, config['WALLET']['LOCATORS']['USER_CARDS'])

        if cards[0].text == config['WALLET']['TEXTS']['ADD_NEW_CARD_TEXT']:

            del cards[0:1]

        return len(cards)

    def clickOnDeleteCardButton(self):
        GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['DELETE_CARD_BUTTON'],
                                    By.XPATH).click()


    def getDeletePopupText(self,):
        text = GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['DELETE_CARD_POPUP'],
                                    By.XPATH).text
        return text


    def clickOnDeleteYes(self):
        GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['DELETE_CARD_YES_BUTTON'],
                                    By.XPATH).click()


    def getDeleteYesButtonText(self):
        text = GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['DELETE_CARD_YES_BUTTON'],
                                    By.XPATH).text
        return text


    def clickOnDeleteNo(self):
        GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['DELETE_CARD_NO_BUTTON'],
                                    By.XPATH).click()

    def getDeleteNoButtonText(self,):
        text = GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['DELETE_CARD_NO_BUTTON'],
                                    By.XPATH).text
        return text


    def getDefaultCardVmark(self):
        element = GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['DEFAULT_CARD_V_MARK'],
                                    By.XPATH)
        return element


    def getWeAcceptCardsText(self):
        we_accept_cards_text = GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['ACCEPTED_CARDS_TEXT_AREA'],
                                    By.XPATH).text
        return we_accept_cards_text


    def getWeAcceptCardsIcons(self):
        GenericPO.driver.remoteWebDriver.find_elements_by_xpath(self, config['WALLET']['LOCATORS']['WALLET_ACCEPTED_CARDS_AREA'])


    def getPciFooterText(self):
        pci_footer_text = GenericPO.driver.findElementBy(self, config['WALLET']['LOCATORS']['PCI_FOOTER_TEXT_AREA'],
                                    By.XPATH).text
        return pci_footer_text


    def getWalletModal(self):
        wallet_modal = GenericPO.driver.waitForVisibilityOfElem(self, config['WALLET']['LOCATORS']['CARDS_SECTION'])

        return wallet_modal


    def closeWallet(self):
        GenericPO.driver.waitForElemToBeClickable(self, config['WALLET']['LOCATORS']['WALLET_X_BUTTON'])


    def addCreditCard(self):

        Account.clickOnPaymentMethods(self)

        Wallet.clickOnAddNewCard(self)

        Wallet.enterCcNumber(self)

        Wallet.enterExpDate(self)

        Wallet.enterCvc(self)

        Wallet.enterPostalCode(self)

        Wallet.clickOnCcApplyButton(self)



    def addCreditCardFromCheckout(self):

        Wallet.clickOnAddNewCard(self)

        Wallet.enterCcNumber(self)

        Wallet.enterExpDate(self)

        Wallet.enterCvc(self)

        Wallet.enterPostalCode(self)

        Wallet.clickOnCcApplyButton(self)
