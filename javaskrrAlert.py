from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class AlertHandle:
    def __init__(self, driver):
        self.driver = driver

    def switchToAlert(self, baseurl):
        driver.get(baseurl)
        driver.implicitly_wait(10)

        driver.find_element(By.ID, "name").send_keys("Playa")
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept()
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Playa")
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)
        alert2 = driver.switch_to.alert
        alert2.dismiss()

        driver.quit()


driver = webdriver.Chrome()
ah = AlertHandle(driver)
baseurl = "https://letskodeit.teachable.com/pages/practice"
ah.switchToAlert(baseurl)
