from selenium import webdriver
import time


class WindowSize:
    def __init__(self, driver):
        self.driver = driver

    def findSize(self, baseurl):
        driver.get(baseurl)

        driver.implicitly_wait(15)
        driver.maximize_window()

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")

        print("Height of the window is: " + str(height))
        print("Width of the window is " + str(width))

    def scroll(self, baseurl):
        driver.get(baseurl)

        driver.implicitly_wait(10)

        driver.execute_script("window.scrollBy(0, 2000);")

        driver.execute_script("window.scrollBy(0, -2000);")
#       driver.execute_script("arguments[0].scrollIntoView(true);" , elementintoview)

#       viewlocation = yourelement.location_once_scrolled_into_view
#       print(str(viewlocation))

        driver.quit()


driver = webdriver.Chrome()
ws = WindowSize(driver)
baseurl = "https://www.thinkdirtyapp.com/verified-brands"
ws.findSize(baseurl)
ws.scroll(baseurl)
