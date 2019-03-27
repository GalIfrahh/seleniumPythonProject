import sys
from multiprocessing import TimeoutError
import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import (NoSuchElementException, TimeoutException)
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
from Services.ErrorService import ErrorsHandler


class DriverWrapper:


    def openSut(self, url):
        self.driver.get(url)


    def closeCurrent(self):
        self.driver.close()


    def closeAll(self):
        self.driver.quit()


    def findElementBy(self, value, LocatorType):
        
        element_assigned = False

        try:
            if LocatorType == By.XPATH:

                element = WebDriverWait(self.driver, 10).until(
                    ec.visibility_of_element_located((By.XPATH, value)))

            elif LocatorType == By.ID:

                element = WebDriverWait(self.driver, 10).until(
                    ec.visibility_of_element_located((By.ID, value)))

            if element is not None:
                element_assigned = True

                
        except TimeoutException as E:
            logging.error(ErrorsHandler.TIMEOUT_ERROR)
            

        except NoSuchElementException as E:
            logging.error(ErrorsHandler.NO_SUCH_ELEMENT)

            
        if element_assigned is True:
            
            return element
        
        else:
            print(ErrorsHandler.ELEMENT_NOT_ASSIGNED_YET)


            
    def hoverAndClick(self, firstElementLocator, secondElementLocator):
        
        action = ActionChains(self.driver)

        action.move_to_element(self.driver.find_element_by_xpath(firstElementLocator)).move_to_element(
            
            (self.driver.find_element_by_xpath(secondElementLocator))).double_click((
            
            self.driver.find_element_by_xpath(secondElementLocator))).perform()


    def selectFromDropDown(self, drop_down_locator, option_text):
        
        selector = Select(self.driver.find_element_by_id(drop_down_locator))
  
        selector.select_by_visible_text(option_text)


    def getDropDownOptionsList(self, drop_down_locator):
        
        selector = Select(self.driver.find_element_by_id(drop_down_locator))

        return selector.options


    def waitForElemToBeClickable(self, elementLocator):
        
        try:
            WebDriverWait(self.driver, 10).until(
                ec.element_to_be_clickable((By.XPATH, elementLocator))).click()

        except TimeoutException:
            print(ErrorsHandler.TIMEOUT_ERROR + " " + ErrorsHandler.ELEMENT_NOT_VISIBLE)


    def waitForInvisibilityOfElem(self, elementLocator):
        
        isVisible = WebDriverWait(self.driver, 5).until(
            ec.invisibility_of_element_located((By.XPATH, elementLocator)))

        return isVisible


    def waitForVisibilityOfElem(self, elementLocator):
        try:
            element = WebDriverWait(self.driver, 7).until(
                ec.visibility_of_element_located((By.XPATH, elementLocator)))

            return element

        except TimeoutException:
            print(ErrorsHandler.TIMEOUT_ERROR + " " + ErrorsHandler.ELEMENT_NOT_VISIBLE)


    def switchToIframe(self, element):
        self.driver.switch_to.frame(element)


    def switchToWindow(self, window_number):
        self.driver.switch_to.window(self.driver.window_handles[window_number])


    def getCurrentUrl(self):
        
        current_url = self.driver.current_url

        return current_url


    def executeScript(self, script_to_execute):
        self.driver.execute_script(script_to_execute)

        
    def refreshPage(self):
        self.driver.refresh()


    def saveScreenShot(self, test_name):
        
        filename = test_name + '_screenShot.png'

        self.driver.save_screenshot(

        '/ScreenShots' + filename)

         return test_name

