from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest
import os

#export PYTHONPATH=$(pwd)
#or
#export PYTHONPATH=$PYTHONPATH
#py.test -s -v tests/home/login_tests.py

class LoginTests(unittest.TestCase):

    baseURL = "https://letskodeit.teachable.com/"
    driverLocation = "C:\\Users\\Parth\\PycharmProjects\\libs\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = driverLocation
    driver = webdriver.Chrome(driverLocation)
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)

    lp = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("gamerboy09pc@gmail.com", "letskodeit")
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.driver.get(self.baseURL)
        self.lp.login("gamerboy09pc@gmail.com", "letskodeit")
        result = self.lp.verifyLoginFailed()
        assert result == True

ff = LoginTests()
ff.test_validLogin()