from Infrastracture.GenericPageObjects import *


class History:


    def getHistoryList(self):

        history_list = self.driver.find_elements_by_xpath(config['HISTORY_SCREEN']['LOCATORS']['HISTORY_ORDERS_LIST'],
                                            By.XPATH)
        return history_list


    def getHistoryFirstOrderPrice(self):

        history_list = GenericPO.driver.find_elements_by_xpath(
                                config['HISTORY_SCREEN']['LOCATORS']['HISTORY_ORDERS_LIST'])

        first_order_price = history_list[0].find_element_by_xpath(config['HISTORY_SCREEN']['LOCATORS']['FIRST_ORDER_PRICE']).text

        return first_order_price
