from Infrastracture.GenericPageObjects import *


class HomePage(GenericPO):


    def clickOnCookiePolicyButton(self):
            GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['COOKIES_POLICY_BTN'],
                                    By.XPATH).click()


    def openSut(self, env):

        if env == "test":
            self.driver.openSut(self, config['SUT']['TEST'])

        elif env == "sand":
            GenericPO.driver.openSut(self, config['SUT']['SAND'])
            

        elif env == "prod":
            GenericPO.driver.openSut(self, config['SUT']['PROD'])


            
    def getSutUrl(self):
        text = GenericPO.driver.getCurrentUrl(self)

        return text

    

    def getCookPolicyTxt(self):
        txt = GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['COOKIES_POLICY_BTN'],
                                                By.XPATH).text
        return txt

    
    def goToAppSiteHeader(self):
        GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['BACK_TO_APP_HEADER_LINK'],
                                          By.XPATH).click()

        
    def getAppLinkText(self):
        app_link_text = GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['BACK_TO_APP_HEADER_LINK'],
                                                       By.XPATH).text
        return app_link_text


    
    def clickOnConnect(self):
        GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['CONNECT_BTN'],
                                    By.ID).click()


    def getLoginButtonText(self):
        text = GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['CONNECT_BTN_TEXT_AREA'],
                                                 By.XPATH).text
        return text


    def getInputsPlaceHolder(self):
        place_holders = [
            GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_PLACE_HOLDER'],
                                           By.XPATH).text,

            GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['SELECT_DATE_PLACE_HOLDER'],
                                           By.XPATH).text,

            GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['SELECT_TIME_PLACE_HOLDER'],
                                           By.XPATH).text]
        
        return place_holders

    
    
    def chooseLocation(self):
        GenericPO.driver.selectFromDropDown(self, config['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_DROP_DOWN'],
                                            config['HOME_PAGE']['DATA']['SECOND_LOCATION'])


    def getLocationsList(self):
        locations_list = GenericPO.driver.getDropDownOptionsList(self,
            config['HOME_PAGE']['LOCATORS']['SELECT_LOCATION_DROP_DOWN'])

        return locations_list

    
    
    def chooseDate(self):
        GenericPO.driver.selectFromDropDown(self, config['HOME_PAGE']['LOCATORS']['SELECT_DATE_DROP_DOWN'],
                                        config['HOME_PAGE']['DATA']['TOMORROW'])


    def chooseTime(self):
        GenericPO.driver.selectFromDropDown(self, config['HOME_PAGE']['LOCATORS']['SELECT_TIME_DROP_DOWN'],
                                        config['HOME_PAGE']['DATA']['TIME'])

        
    def getStartOrderPopup(self):
        element = GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['START_ORDER_POPUP_TEXT_AREA'],
                                    By.XPATH)
        return element


    def clickOnStartOrderPopupButton(self):
        GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['START_ORDER_POPUP_BUTTON'],
                                    By.XPATH).click()


        
    def clickOnTermsAndConditions(self):
        GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['TERMS_AND_COND_BUTTON'],
                                    By.XPATH).click()


    def ClIckOnPrivacyPolicy(self):
        GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['PRIVACY_POLICY'],
                                          By.XPATH).click()


    def getFooterTxt(self):

        footer_texts = [GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['FOOTER_FIRST_PART'],
                                                By.XPATH).text,
                      GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['FOOTER_SECOND_PART'],
                                                By.XPATH).text,
                      GenericPO.driver.findElementBy(self, config['HOME_PAGE']['LOCATORS']['FOOTER_THIRD_PART'],
                                                By.XPATH).text]
        return footer_texts

