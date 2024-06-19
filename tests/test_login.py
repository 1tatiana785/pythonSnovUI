import allure
import pytest
from base.base_test import BaseTest
from config.links import *
from config.data import *


@allure.feature("BEV Functionality")
class TestLogin(BaseTest):

    @allure.title("Login")
    @allure.severity("Critical")
    @pytest.mark.skip
    def test_login(self):
        self.login_page.open(Links.LOGIN_PAGE)
        print("q")
        self.login_page.enter_email(Data.LOGIN)
        self.login_page.enter_password(Data.PASSWORD)
        self.login_page.click_login_button()

    @allure.title("Check balance")
    @allure.severity("Critical")
    def test_check_balance(self):
        self.login_page.login(Links.BEV_PAGE, Data.LOGIN, Data.PASSWORD)
        self.login_page.check_balance()
