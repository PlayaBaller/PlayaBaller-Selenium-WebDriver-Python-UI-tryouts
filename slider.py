from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class SliderHandle:
    def __init__(self, driver):
        self.driver = driver

    def sliderdrag(self):
        baseurl = 'https://jqueryui.com/slider/'
        driver.get(baseurl)

        iframetoswitch = driver.find_element_by_xpath("//iframe[@class='demo-frame']")

        driver.switch_to.frame(iframetoswitch)
        print("Switched to frame")

        slider = driver.find_element_by_xpath("//div[@id='slider']//span")

        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(slider, 200, 0).perform()
            actions.drag_and_drop_by_offset(slider, -100, 0).perform()
            actions.drag_and_drop_by_offset(slider, 200, 0).perform()
            print("Sliding!")
            time.sleep(10)
        except:
            print("Failed to slide")

        driver.quit()


driver = webdriver.Chrome()
sh = SliderHandle(driver)
sh.sliderdrag()
