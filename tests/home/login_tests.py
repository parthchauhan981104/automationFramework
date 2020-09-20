from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest

#export PYTHONPATH=$(pwd)
#or
#export PYTHONPATH=$PYTHONPATH
#py.test -s -v tests/home/login_tests.py --browser chrome

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("gamerboy09pc@gmail.com", "letskodeit")
        result = self.lp.verifyLoginSuccessful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("gamerboy09pc@gmail.com", "letskodeit")
        result = self.lp.verifyLoginFailed()
        assert result == True


