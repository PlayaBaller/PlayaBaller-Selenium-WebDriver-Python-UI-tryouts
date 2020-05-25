from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class HiddenElems:
    def findHidden(self):
        baseurl = "https://learn.letskodeit.com/p/practice"

        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.implicitly_wait(5)

        textboxelem = driver.find_element_by_id("displayed-text")
        textboxstate = textboxelem.is_displayed()

        if textboxstate is True:
                print(str(textboxstate))
        else:
            print("Element is hidden" + str(textboxstate))
        time.sleep(3)

        driver.find_element_by_id("hide-textbox").click()

        textboxstate = textboxelem.is_displayed()
        print(str(textboxstate))
        time.sleep(3)

        driver.find_element_by_id("show-textbox").click()
        textboxstate = textboxelem.is_displayed()
        print(str(textboxstate))
        time.sleep(3)

        driver.quit()

    def testExpedia(self):
        baseurl = "https://www.expedia.com/"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        driver.find_element_by_xpath("//span[contains(text(),'Flights')]").click()
        drpdwnelem = driver.find_element_by_xpath("//div[@id='traveler-selector-hp-flight']//button[@class="
                                                  "'trigger-utility menu-trigger btn-utility btn-secondary dropdown-"
                                                  "toggle theme-standard pin-left menu-arrow gcw-component "
                                                  "gcw-traveler-amount-select gcw-component-initialized']")
        if drpdwnelem is not None:
            print("Elem is found")
        else:
            print("Element is not found")
        driver.implicitly_wait(3)

        drpdwnelem.click()

        driver.implicitly_wait(2)

        childrenplus = driver.find_element_by_xpath("//div[@class='traveler-selector-sinlge-room-data "
                                                    "traveler-selector-room-data']//div[@class='children-wrapper']"
                                                    "//div[@class='uitk-grid step-input-outside gcw-component"
                                                    " gcw-component-step-input "
                                                    "gcw-step-input gcw-component-initialized']//button"
                                                    "[@class='uitk-step-input-button uitk-step-input-plus']//span"
                                                    "[@class='uitk-icon']//*[local-name()='svg']")

        if childrenplus is not None:
            print("Drop-down element is found")
        else:
            print("Drop-down element is not found")

        driver.implicitly_wait(2)

        childrenplus.click()
        print(str(childrenplus.is_displayed()))
        driver.quit()


he = HiddenElems()
he.findHidden()
he.testExpedia()
