from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import os

#export PYTHONPATH=$(pwd)
#or
#export PYTHONPATH=$PYTHONPATH
#py.test -s -v tests/home/login_tests.py

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL = "https://letskodeit.teachable.com/"
        driverLocation = "C:\\Users\\Parth\\PycharmProjects\\libs\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("gamerboy09pc@gmail.com", "letskodeit")

        userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']")
        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

ff = LoginTests()
ff.test_validLogin()