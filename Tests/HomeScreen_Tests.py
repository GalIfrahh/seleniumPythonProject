import time

import pytest
from pytest_testconfig import config
from Infrastracture.Base_Test import BaseTest
from PageObjects.ConnectPO import Connect
from PageObjects.EnterPhoneScreenPO import EnterPhoneScreen
from PageObjects.HomePO import HomePage
from Services.ErrorService import ErrorsHandler


class HomeScreen_Tests(BaseTest):
    pass
    # def test_100_openSut(self, env):
    #
    #     current_app_link = HomePage.getSutUrl(self)
    #
    #     expected_app_url = config['SUT'][env.upper()]
    #
    #     assert current_app_link == expected_app_url
    #
    #
    # @pytest.mark.skipif(config['HOME_PAGE']['LOCATORS']['BACK_TO_APP_HEADER_LINK'] == 0,
    #                  reason=ErrorsHandler.FEATURE_NOT_EXIST_ON_APP)
    # def test_101_checkClientLink(self):
    #
    #     HomePage.clickOnCookiePolicyButton(self)
    #
    #     current_app_link_text = HomePage.getAppLinkText(self)
    #
    #     expected_app_link_text = config['HOME_PAGE']['TEXTS']['BACK_TO_APP_HEADER_LINK_TEXT']
    #
    #     assert current_app_link_text == expected_app_link_text
    #
    # def test_102_getInputsPlaceHolders(self):
    #
    #     inputs_place_holders = HomePage.getInputsPlaceHolder(self)
    #
    #     assert inputs_place_holders[0] == config['HOME_PAGE']['TEXTS']['SELECT_LOCATION_PLACE_HOLDER_TEXT']
    #
    #     assert inputs_place_holders[1] == config['HOME_PAGE']['TEXTS']['SELECT_DATE_PLACE_HOLDER_TEXT']
    #
    #     assert inputs_place_holders[2] == config['HOME_PAGE']['TEXTS']['SELECT_TIME_PLACE_HOLDER_TEXT']
    #
    # def test_103_CheckInputsWithData(self):
    #
    #     HomePage.clickOnCookiePolicyButton(self)
    #
    #     HomePage.chooseLocation(self)
    #
    #
    # def test_104_checkLocationList(self):
    #
    #     Connect.login(self)
    #
    #     locations_list = HomePage.getLocationsList(self)
    #
    #     expected_location_number = 0
    #
    #     for location in locations_list:
    #
    #         assert location.text == config['HOME_PAGE']['DATA']['FULL_LOCATIONS_NAMES'][expected_location_number]
    #
    #         expected_location_number += 1
    #
    # def test_104_connectButton(self):
    #
    #     HomePage.clickOnCookiePolicyButton(self)
    #
    #     HomePage.clickOnConnect(self)
    #
    #     assert EnterPhoneScreen.getPhoneFieldElement(self).is_displayed()
    #
    # def test_105_footerText(self):
    #
    #     HomePage.clickOnCookiePolicyButton(self)
    #
    #     current_footer_text = HomePage.getFooterTxt(self)[0]
    #
    #     expected_footer_text = config['HOME_PAGE']['TEXTS']['FOOTER_FIRST_PART_TEXT']
    #
    #     assert current_footer_text + "s" == expected_footer_text
