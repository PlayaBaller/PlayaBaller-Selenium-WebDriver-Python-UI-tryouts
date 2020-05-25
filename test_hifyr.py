from selenium import webdriver


class TestBasic:
    def __init__(self, driver):
        self.driver = driver

    def test_openAndCompare(self, baseurl):
        driver.get(baseurl)

        driver.implicitly_wait(3)

        rpsection = driver.find_element_by_xpath("//a[contains(text(),'Retail Platform')]")

        if rpsection is not None:
            print(f"{rpsection} element is found")
        else:
            print(f"{rpsection} element is not found")

        rpsection.click()

        driver.implicitly_wait(10)

        retailplatformcomponents = driver.find_element_by_xpath("//*[@class='icon-button bounce-down mt-2']"
                                                                "[contains(text(),'Components')]")

        retailplatformcomponents.click()
        forlog = retailplatformcomponents.is_enabled()
        print(str(forlog))

        sectionactivedat = driver.find_element_by_xpath("//h5[contains(text(),'Active Data')]")
        forlog2 = sectionactivedat.is_enabled()
        print(str(forlog2))

        sectionactivedat.click()

        driver.implicitly_wait(5)

        desiredtext = driver.find_element_by_xpath("//p[contains(text(),'The ERP Lite will include connectors "
                                                   "to most popul')]")
        forlog3 = desiredtext.is_enabled()
        print(str(forlog3))

        if forlog3 is True:
            print('The desired text is present')
        else:
            print('The desired text is not found')

        driver.close()
        driver.quit()

        return forlog, forlog2, forlog3


driver = webdriver.Chrome()
bt = TestBasic(driver)
baseurl = "https://hifyreretail.com/"
bt.test_openAndCompare(baseurl)
