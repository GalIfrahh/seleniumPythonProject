import time

import pytest
from pytest_testconfig import config
from Infrastracture.Base_Test import BaseTest
from PageObjects.ConnectPO import Connect
from PageObjects.HomePO import HomePage
from Services.ErrorService import ErrorsHandler


class ConnectTests(BaseTest):
    pass

     def test_100_registration(self):
     
          Connect.register(self)
     
          current_login_button_text = HomePage.getLoginButtonText(self)
     
          before_login_button_text = config['HOME_PAGE']['TEXTS']['CONNECT_BUTTON_BEFORE_LOGIN']
     
          self.assertTrue(current_login_button_text != before_login_button_text, ErrorsHandler.LOGIN_ERROR + " " +
                          current_login_button_text)
    
    # def test_101_login(self):
    #
    #     Connect.login(self)
    #
    #     current_login_button_text = HomePage.getLoginButtonText(self)
    #
    #     before_login_button_text = config['HOME_PAGE']['TEXTS']['CONNECT_BUTTON_BEFORE_LOGIN']
    #
    #     assert current_login_button_text != before_login_button_text
    #
    # def test_102_logout(self):
    #
    #     # login
    #     Connect.login(self)
    #
    #     current_login_button_text = HomePage.getLoginButtonText(self)
    #
    #     before_login_button_text = config['HOME_PAGE']['TEXTS']['CONNECT_BUTTON_BEFORE_LOGIN']
    #
    #     assert current_login_button_text != before_login_button_text
    #
    #     # logout
    #     Connect.logout(self)
    #
    #     current_login_button_text = HomePage.getLoginButtonText(self)
    #
    #     assert current_login_button_text == before_login_button_text
    #
    # def test_103_checkMigration(self):
    #     pass
