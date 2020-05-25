from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time


class GetText:
    def findInnertext(self):
        baseurl = "https://www.airspacemag.com/"

        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        desiredel = driver.find_element_by_xpath("//div[@class='nav-btn-item selected']//a[@class='nav-btn']"
                                                 "[contains(text(),'Homepage')]").get_attribute("innerText")

        print(desiredel)


gt = GetText()
gt.findInnertext()

