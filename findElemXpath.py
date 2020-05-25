from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FindByXpath:
    def find(self):
        baseurl = "https://www.reddit.com/"

        driver = webdriver.Chrome()
        driver.get(baseurl)
        elementbyxpath = driver.find_element(By.XPATH, "//*[@class='_1hdDhVEGWEdVJcgy2XQ2Eq']")
        
        if elementbyxpath is not None:
            print("Element is found by Xpath")
        else:
            print("Cannot find element by specified Xpath")

        elementbylinktext = driver.find_element(By.CLASS_NAME, "_3ryJoIoycVkA88fy40qNJc")
        if elementbylinktext is not None:
            print("Element is found by specified class name")
        else:
            print("Cannot find element by specified class name")

        time.sleep(20)


ff = FindByXpath()
ff.find()
