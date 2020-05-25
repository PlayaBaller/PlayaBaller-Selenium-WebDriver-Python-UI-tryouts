from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class IframeHandle:
    def __init__(self, driver):
        self.driver = driver

    def iframeSwitch(self, baseurl):
        driver.get(baseurl)
        driver.implicitly_wait(15)

#        iframetoswitch = driver.find_element_by_xpath("//iframe[@name='google_ads_iframe_"
#                                                      "/22152718/sws-hb//w3schools.com//main_leaderboard_0']")
#        driver.implicitly_wait(10)

        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@name='google_ads_iframe_"
                                                             "/22152718/sws-hb//w3schools.com//main_leaderboard_0']"))
        print("Currently, focusing on Iframe content")

        driver.switch_to.default_content()
        print("Going back to the main window")


driver = webdriver.Chrome()
ws = IframeHandle(driver)
baseurl = "https://www.w3schools.com/html/html_iframe.asp"
ws.iframeSwitch(baseurl)
