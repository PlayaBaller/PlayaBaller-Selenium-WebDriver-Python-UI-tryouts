from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class MHov:
    def __init__(self, driver):
        self.driver = driver

    def mouseHov(self, baseurl):
        driver.get(baseurl)
        driver.implicitly_wait(8)

        driver.execute_script("window.scrollBy(0, 600);")

        itemuponhow = driver.find_element_by_id("mousehover")

        try:
            hovaction = ActionChains(driver)
            hovaction.move_to_element(itemuponhow).perform()
            print(f"Hovered on the {itemuponhow} element")
            eluponhover = driver.find_element_by_xpath("//a[contains(text(),'Reload')]")
            eluponhover.click()
            print(f"{eluponhover} Clicked")
        except:
            print("Failed to hover on the element")


driver = webdriver.Chrome()
mh = MHov(driver)
baseurl = "https://letskodeit.teachable.com/pages/practice"
mh.mouseHov(baseurl)
