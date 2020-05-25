from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time


class GetAttribute:
    def findAttribute(self):
        baseurl = "https://www.airspacemag.com/"

        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        desiredel = driver.find_element_by_xpath("//a[contains(text(),'Reaching the "
                                                 "Singularity May be Humanity')]").get_attribute("href")
        # or desiredel = driver.find_element_by_xpath("//a[contains(text(),
        # 'Reaching the Singularity May be Humanity')]")
        #    attribute = desiredel.get_attribute()
        #    print(attribute)

        print(desiredel)


gt = GetAttribute()
gt.findAttribute()

