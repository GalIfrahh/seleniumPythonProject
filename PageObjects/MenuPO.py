from Infrastracture.GenericPageObjects import *


class Menu:


    def chooseFirstCategory(self):
        time.sleep(1)
        GenericPO.driver.findElementBy(config['MENU']['LOCATORS']['FIRST_CATEGORY'], By.XPATH).click()

    @staticmethod
    def chooseSecondCategory():
        GenericPO.driver.findElementBy(config['MENU']['LOCATORS']['SECOND_CATEGORY'], By.XPATH).click()

    @staticmethod
    def checkIfCategoryChosen():
        isChosen = False

        if GenericPO.driver.findElementBy(config['MENU']['LOCATORS']['SECOND_CATEGORY_ACTIVE'], By.XPATH) is not None:
            isChosen = True

        return isChosen

    @staticmethod
    def chooseRestrictedAgeCategory():
        time.sleep(1)
        GenericPO.driver.findElementBy(config['MENU']['DATA']['AGE_RESTRICTED_CATEGORY'], By.XPATH).click()


    def chooseUpSaleItem(self):
        GenericPO.driver.findElementBy(self, config['MENU']['LOCATORS']['UP_SALE_ITEM'], By.XPATH).click()


    def firstCategoryText(self):
        text = GenericPO.driver.findElementBy(self, config['MENU']['LOCATORS']['FIRST_CATEGORY'], By.XPATH).text
        return text


    def chooseSecondItem(self):
        time.sleep(1)
        GenericPO.driver.findElementBy(self, config['MENU']['LOCATORS']['SECOND_ITEM'],
                                          By.XPATH).click()



    def clickOnMenuToast(self):
        if BasicTestClass.platform == 'mobile':
            time.sleep(1)
            GenericPO.webDriver.findElementBy(self, config['MENU']['LOCATORS']['MENU_TOAST'],
                                          By.XPATH).click()
            time.sleep(1)


    def getSecondItemText(self):
        text = GenericPO.driver.findElementBy(self, config['MENU']['LOCATORS']['SECOND_ITEM'],
                                          By.XPATH).text
        return text


    def getCartSecondItemText(self):
        text = GenericPO.driver.findElementBy(self, config['MENU']['LOCATORS']['CART_SECOND_ITEM_TEXT'],
                                          By.XPATH).text
        return text


    def getTotalPrice(self):

        price = GenericPO.driver.findElementBy(self, config['MENU']['LOCATORS']['CART_TOTAL'],
                                          By.XPATH).text

        return price


    def clickOnEditItem(self):
        GenericPO.driver.findElementBy(self, config['MENU']['LOCATORS']['EDIT_ITEM_BUTTON'],
                                    By.XPATH).click()

    def clickOnEditItemFromCart(self):
        GenericPO.driver.findElementBy(self, config['MENU']['LOCATORS']['EDIT_ITEM_FROM_CART'],
                                    By.XPATH).click()


    def getModifiersModal(self):
        modifier_modal = GenericPO.driver.findElementBy(self, config['MENU']['LOCATORS']['MODIFIER_MODAL'],
                                                       By.XPATH)
        return modifier_modal


    def getModifiersModalHeaderText(self):
        header_text = GenericPO.driver.findElementBy(config['MENU']['LOCATORS']['MODIFIER_MODAL_HEADER'],
                                          By.XPATH).text
        return header_text

    def closeModifiersWindow(self):
        time.sleep(1)
        GenericPO.driver.findElementBy(self, config['MENU']['LOCATORS']['CLOSE_MODIFIER_X_BUTTON'],
                                          By.XPATH).click()

    def deleteItemFromCart(self):
        GenericPO.driver.findElementBy(config['MENU']['LOCATORS']['DELETE_ITEM_FROM_CART'],
                                          By.XPATH).click()


    def getCartItemsList(self):
        cart_items_list = self.driver.find_elements_by_xpath(config['MENU']['LOCATORS']['CART_ITEMS_CONTAINER'])

        return cart_items_list


    def getModifiersBySection(self):
        time.sleep(1)

        modifiers_list = self.driver.find_elements(by=By.XPATH, value=config['MENU']['LOCATORS']['SECOND_CATEGORY_MODIFIERS'])

        return modifiers_list


    def checkModifierActivity(self, element):
        is_active = False

        if element.find_element_by_xpath(config['MENU']['LOCATORS']['ACTIVE_MODIFIER']) is not None:
            is_active = True

        return is_active


    def moveToCart(self, platform):

        if platform == 'mobile':
            time.sleep(1)
            GenericPO.driver.findElementBy(self, "//div[@id='toast-container']",
                                        By.XPATH).click()
            time.sleep(1)

            GenericPO.driver.findElementBy(self, config['MENU']['LOCATORS']['MOBILE_CART_ICON'],
                                        By.XPATH).click()


    def clickOnProceedToCheckout(self):

        #if BasicTestClass.platform == "desktop":

                GenericPO.driver.findElementBy(self, config['MENU']['LOCATORS']['PROCEED_TO_CHECKOUT_BUTTON'],
                                              By.XPATH).click()

        #elif BasicTestClass.platform == "mobile":

                # GenericPO.webDriver.findElementBy("//div[@id='toast-container']",
                #                                   LocatorsType=LocatorsTypes.XPATH).click()
                # time.sleep(1)
                #
                # GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['MOBILE_CART_ICON'],
                #                                   LocatorsType=LocatorsTypes.XPATH).click()

                # GenericPO.webDriver.findElementBy(params['MENU']['LOCATORS']['PROCEED_TO_CHECKOUT_BUTTON'],
                #                               LocatorsType=LocatorsTypes.XPATH).click()


    def getPopup(self):
        screen_popup = GenericPO.webDriver.waitForVisibilityOfElem(
            self, config['MENU']['LOCATORS']['SCREEN_POPUP'])

        return screen_popup


    def getPopupHeaderText(self):
        screen_popup_header_text = GenericPO.webDriver.waitForVisibilityOfElem(self,
            config['MENU']['LOCATORS']['SCREEN_POPUP_HEADER']).text

        return screen_popup_header_text


    def getPopupText(self):
        screen_popup_text = GenericPO.webDriver.waitForVisibilityOfElem(self,
            config['MENU']['LOCATORS']['SCREEN_POPUP_BODY']).text

        return screen_popup_text


    def getUpSalePopupText(self):
        up_sale_popup_text = GenericPO.webDriver.waitForVisibilityOfElem(self,
            config['MENU']['LOCATORS']['UP_SALE_POPUP_BODY']).text

        return up_sale_popup_text

    def clickOnPopupOkBtn(self):
        GenericPO.driver.findElementBy(self,
             config['MENU']['LOCATORS']['SCREEN_POPUP_OK'], By.XPATH).click()
