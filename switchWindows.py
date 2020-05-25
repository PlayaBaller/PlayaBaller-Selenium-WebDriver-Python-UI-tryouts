from selenium import webdriver
import time


class SwitchWindows:
    def __init__(self, driver):
        self.driver = driver

    def sitchw(self, baseurl):
        driver.get(baseurl)

        driver.implicitly_wait(10)

        parenthandle = driver.current_window_handle
        print("Parent handle " + str(parenthandle))

        driver.find_element_by_id("openwindow").click()

        allhandles = driver.window_handles

        for handle in allhandles:
            print("Switched to " + str(handle))
            if handle not in parenthandle:
                driver.switch_to.window(handle)
                print("Browser switched to :" + handle)
                searchbox = driver.find_element_by_id("search-courses")
                searchbox.send_keys("HustleHustleHustleHustleHustle")
                time.sleep(5)
                driver.close()
                break

        driver.switch_to.window(parenthandle)
        print("Switched to the main window")

        driver.find_element_by_id("name").send_keys("HustleHustleHustle")


driver = webdriver.Chrome()
ws = SwitchWindows(driver)
baseurl = "https://learn.letskodeit.com/p/practice"
ws.sitchw(baseurl)
