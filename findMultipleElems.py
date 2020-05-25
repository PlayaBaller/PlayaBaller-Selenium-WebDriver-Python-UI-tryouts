from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FindElemsList:
    def find(self):
        baseurl = "https://www.reddit.com/"

        driver = webdriver.Chrome()
        driver.get(baseurl)
        
        elemslist = driver.find_elements_by_class_name("_2-aCCpAklEV0DkVWrpodjE")
        lenght = len(elemslist)

        if elemslist is not None:
            print('Elements found')
            print("Size of the elements list is " + str(lenght))
        else:
            print("Cannot find any elements")

        time.sleep(20)


ff = FindElemsList()
ff.find()
