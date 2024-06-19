import allure
import pytest
from base.base_test import BaseTest
from config.links import *
from config.data import *


@allure.feature("BEV Functionality")
class TestBEV(BaseTest):

    @allure.title("Load more")
    @allure.severity("Critical")
    @pytest.mark.parametrize('file', Data.files)
    @pytest.mark.skip
    def test_upload_error_file(self, file):
        self.login_page.login(Links.BEV_PAGE, Data.LOGIN, Data.PASSWORD)
        self.bev_page.upload_file(file)

    @allure.title("Load more")
    @allure.severity("Critical")
    def test_load_more(self):
        self.login_page.login(Links.BEV_PAGE, Data.LOGIN, Data.PASSWORD)
        self.bev_page.load_more()
        self.bev_page.make_screenshot("loadMore")

    @allure.title("Add to list")
    @allure.severity("Critical")
    @pytest.mark.skip
    def test_add_to_list(self):
        self.login_page.login(Links.BEV_PAGE, Data.LOGIN, Data.PASSWORD)
        self.bev_page.add_manually("Name", "name@gmail.com")
        self.bev_page.add_to_list()

    @allure.title("Download")
    @allure.severity("Critical")
    @pytest.mark.skip
    def test_download(self):
        self.login_page.login(Links.BEV_PAGE, Data.LOGIN, Data.PASSWORD)
        self.bev_page.download()
