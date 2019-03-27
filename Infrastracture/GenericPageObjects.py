import pytest
from Infrastracture.Base_Test import BaseTest
from Infrastracture.WebDriverWrapper import DriverWrapper
from selenium.webdriver.common.by import By
import time
from pytest_testconfig import config


class GenericPO():

    driver = BaseTest.driver
