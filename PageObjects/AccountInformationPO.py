from Infrastracture.GenericPageObjects import *


class AccountInformation:

    def getNameText(self):
        text = GenericPO.driver.findElementBy(self, "//*[@id='modal-body']/div/div[1]/div/input",
                                              By.XPATH).text
        return text
