from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import logging
from basicWeb.custom_logger import customLogger as cl
import unittest


class TestLogin(object):
    def __init__(self, driver):
        self.driver = driver

    def test_openAndLogin(self):
        log = cl(logging.DEBUG)
        log.info("Method openAndLogin is started")

        baseurl = 'https://trello.com/'
        driver.get(baseurl)

        driver.implicitly_wait(5)

        login = driver.find_element_by_xpath("//*[local-name() = 'a' and contains (@class, "
                                             "'btn btn-sm btn-link text-white')]")

        login.click()

        driver.implicitly_wait(5)

        user = driver.find_element_by_xpath("//input[@id='user']")
        user.clear()
        user.send_keys("*")

        pwd = driver.find_element_by_xpath("//input[@id='password']")
        pwd.clear()
        pwd.send_keys("*")

        confirm = driver.find_element_by_xpath("//input[@id='login']")
        confirm.click()

        driver.implicitly_wait(5)

        board = driver.find_element_by_xpath("//li[@class='boards-page-board-section-list-item']//a[@class='board-tile "
                                             "mod-light-background']//div[@class='board-tile-details-sub-container']")
        board.click()

        createcard = driver.find_element_by_xpath("//body/div[@id='trello-root']/div[@id='chrome-container']"
                                                  "/div[@class='BfrybzRYI4wt4w']"
                                                  "/div[@id='surface']"
                                                  "/main[@id='popover-boundary']/div[@id='content']"
                                                  "/div[@class='board-wrapper']"
                                                  "/div[@class='board-main-content']/div[@class='board-canvas']"
                                                  "/div[@id='board']/div[1]/div[1]/div[3]/a[1]")

        driver.implicitly_wait(1)

        createcard.click()

        cardtitle = driver.find_element_by_xpath("//textarea[@placeholder='Enter a title for this card…']")
        cardtitle.send_keys("Created with Python3 & Webdriver")

        cardcreateconfirm = driver.find_element_by_xpath("//input[@class='primary confirm mod-compact js-add-card']")
        cardcreateconfirm.click()
        log.info("Method openAndLogin is done")


driver = webdriver.Firefox()

# ln = Login(driver)

# ln.openAndLogin()
