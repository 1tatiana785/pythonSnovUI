import pytest

from pages.login_page import LoginPage
from pages.bev_page import BEVPage
from base.scroll import Scroll


class BaseTest:
    login_page: LoginPage
    bev_page: BEVPage
    scroll: Scroll

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.bev_page = BEVPage(driver)
        request.cls.scroll = Scroll
