from selenium import webdriver
from selenium.webdriver.common.by import By
from basicWeb.basicWrappers import FirstWrapper
import time
import logging


class UsingWrapper:

    def test(self):
        baseurl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        usedwrapper = FirstWrapper(driver)
        driver.get(baseurl)

        element = usedwrapper.getElement("name")
        print(str(element))

        element.send_keys("SendSendSend")
        time.sleep(10)
        element.clear()

        element2 = usedwrapper.getElement("//input[@id='name']", locatortype="xpath")
        print(str(element2))

        element2.send_keys("Again and again and again")
        time.sleep(5)
        element2.clear()

        print("Finish")
        driver.close()
        driver.quit()


uw = UsingWrapper()
uw.test()



