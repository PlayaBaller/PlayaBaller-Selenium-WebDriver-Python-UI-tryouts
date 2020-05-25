from selenium import webdriver
import requests


class ScrollDown:
    def __init__(self, driver):
        self.driver = driver

    def scroll(self):
        fronturl = 'https://www.upwork.com/jobs/~011ea9254927e578f7'
        driver.get(fronturl)

        driver.add_cookie({'name': "master_access_token",
                           'value': "*"})

        option = driver.find_element_by_xpath("//a[contains(text(),'Sign in')]")
        option.click()

        driver.implicitly_wait(5)

#        searchbox.send_keys("Python-Selenium-Developer")
        driver.execute_script("window.scrollBy(0, 4000);")

        print("Scrolled")


driver = webdriver.Chrome()
scr = ScrollDown(driver)
scr.scroll()
