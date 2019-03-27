from Infrastracture.GenericPageObjects import *
from Services.utils import ProjectUtils


class EnterEmailPage:

    def enterUnExistEmail(self):
        un_exist_email = ProjectUtils.createRandomMail()
        GenericPO.driver.findElementBy(self, config['ENTER_EMAIL_PAGE']['LOCATORS']['ENTER_EMAIL_FIELD'],
                                  By.XPATH).send_keys(un_exist_email)


    def submitEmail(self):
        self.driver.findElementBy(self, config['ENTER_EMAIL_PAGE']['LOCATORS']['SUBMIT_EMAIL_BUTTON'],
                                  By.XPATH).click()
