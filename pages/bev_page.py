import os

import allure
from base.base_page import BasePage

from selenium.webdriver.support import expected_conditions as EC
import time


class BEVPage(BasePage):
    MANUALLY_TAB = ("css selector", ".choice__item:nth-child(2)")
    PROSPECT_LIST_NAME = ("css selector", " .input-label:nth-child(1) input")
    EMAIL_ADDRESS = ("css selector", ".input-label:nth-child(2) textarea")
    VERIFY_EMAIL_BUTTON = ("css selector", ".btn-snovio--single")
    COMPLETE = ("css selector", "tbody tr:nth-child(1) td:nth-child(2) div img.cell__img")

    # upload file
    CHOOSE_FILE = ("xpath", "//input[@type='file']")
    ERROR_TEXT = ("css selector", ".error")

    # export
    DOWNLOAD_BUTTON = ("css selector", "tr:first-child .table__rules:first-child svg:not(.rules-cell__btn--red)")
    DELETE_BUTTON = ".table__box tbody tr:first-child .table__rules>svg:is(.table__rules-btn--red)"
    IFRAME = ("tag name", "iframe")
    EXPORT_EMAIL_INPUT = ("xpath", "//div[@class='modal-snovio export']//label[@class='snovio-checkbox']")
    EXPORT_RADIO1 = ("xpath", "//div[@class='export__extention']//label[2]/input[@type='radio']")
    EXPORT_POPUP = ("css selector", ".export")
    DOWNLOAD = ("xpath", "//div[@class='modal-snovio export']//*[@data-test='modal-confirm']")
    DOWNLOAD_TEXT = ("css selector", ".btn-snovio--export")
    # add to list
    ADD_TO_LIST_BUTTON = ("xpath", "//tr[1]//div[contains(@class,'add-list')]/button")
    FIRST_NAME_LIST = ("css selector", ".app-dropdown__drop-item:nth-child(2)")
    DROPDOWN = ("css selector", ".app-dropdown__drop")
    # load more
    LOAD_MORE = ("css selector", ".pagination .pagination__cell--big")

    @allure.step("Upload file")
    def upload_file(self, file):
        self.wait.until(EC.presence_of_element_located(self.PROFILE))
        self.wait.until(EC.presence_of_element_located(self.CHOOSE_FILE)).send_keys(f"{os.getcwd()}/downloads/"+file)
        time.sleep(3)

    @allure.step("Check error text")
    def check_error(self, text):
        error = self.wait.until(EC.presence_of_element_located(self.ERROR_TEXT)).text()
        print(error)
        assert error == text

    @allure.step("Add manually")
    def add_manually(self, name, email):
        self.wait.until(EC.presence_of_element_located(self.PROFILE))
        self.driver.find_element(*self.MANUALLY_TAB).click()
        self.wait.until(EC.presence_of_element_located(self.PROSPECT_LIST_NAME)).send_keys(name)
        self.driver.find_element(*self.EMAIL_ADDRESS).send_keys(email)
        self.wait.until(EC.element_to_be_clickable(self.VERIFY_EMAIL_BUTTON)).click()
        self.wait.until(EC.invisibility_of_element_located(self.COMPLETE))
        self.wait.until(EC.presence_of_element_located(self.COMPLETE))

    @allure.step("Add to list")
    def add_to_list(self):
        button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_LIST_BUTTON))
        button.click()
        time.sleep(4)
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_LIST)).click()

    @allure.step("Click load more button")
    def load_more(self):
        self.wait.until(EC.presence_of_element_located(self.PROFILE))
        self.action.move_to_element(self.driver.find_element(*self.LOAD_MORE)) \
            .click() \
            .perform()

    @allure.step("Click download icon")
    def download(self):
        self.wait.until(EC.presence_of_element_located(self.PROFILE))
        self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD_BUTTON)).click()
        self.wait.until(EC.presence_of_element_located(self.EXPORT_POPUP))
        self.wait.until(EC.element_to_be_clickable(self.EXPORT_EMAIL_INPUT)).click()
        self.wait.until(EC.element_to_be_clickable(self.DOWNLOAD)).click()
        self.wait.until(EC.presence_of_element_located(self.DOWNLOAD_TEXT)).click()
