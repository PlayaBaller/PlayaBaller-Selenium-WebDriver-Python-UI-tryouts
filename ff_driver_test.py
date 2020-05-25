from selenium import webdriver


class RunFFTests:
    def openFire(self):
        driver = webdriver.Firefox(executable_path="C:\\webdrivers\\geckodriver.exe")
        driver.get("https://github.com/mozilla/geckodriver/releases")


ff = RunFFTests()
ff.openFire()
