from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from basicWeb.test_loginOnPr import TestLogin, driver
from selenium.webdriver import ActionChains
import logging
from basicWeb.custom_logger import customLogger as cl
import unittest


class TestDragnDrop(TestLogin):

    def __init__(self):
        TestLogin.__init__(self, driver)

    def test_openAndLogin(self):
        #   logging.basicConfig(filename="test.log", level=logging.DEBUG)

        logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=logging.DEBUG)
        logging.info("Method of a child class is started")

        super(TestDragnDrop, self).test_openAndLogin()

        todrag = driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']"
                                              "/div/div[@id='surface']/main[@id='popover-boundary']"
                                              "/div[@id='content']/div/div/div/div[@id='board']"
                                              "/div[1]/div[1]/div[2]/a[1]")

        wheretodrop = driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']"
                                                   "/div/div[@id='surface']/main[@id='popover-boundary']"
                                                   "/div[@id='content']/div/div/div/div[@id='board']/div[4]"
                                                   "/div[1]/div[2]/a[1]")

        try:
            ddaction = ActionChains(driver)
#           One complete drag and drop action:
#            ddaction.drag_and_drop(todrag, wheretodrop).perform()
#           OR chain of actions:
            ddaction.click_and_hold(todrag).move_to_element(wheretodrop).release().perform()
            print(f"Desired element {todrag} is relocated")
        except:
            print("Unable to perform drag and drop action")

        print("Daymn, daymn, daaaaaaymn!!!!!!!!!!")

        logging.info("All done, playa")
        driver.quit()


dd = TestDragnDrop()
dd.test_openAndLogin()








