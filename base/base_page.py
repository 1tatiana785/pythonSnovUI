import allure

from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from scroll import Scroll
from config.links import *


class BasePage:
    PAGE_URL = Links.LOGIN_PAGE
    PROFILE = ("css selector", ".snovProfile__toggle-container")
    PROFILE_MENU = ("css selector", ".snovProfile__menu")
    BALANCE = ("css selector", ".snovProfile__limit:nth-child(1) .snovProfile__limit-label")
    LOGOUT_MENU = ("xpath", "//div[@data-logout]")

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)
        self.wait = WebDriverWait(driver, 50, poll_frequency=1)
        self.scroll = Scroll(driver, self.action)

    def open(self, url):
        self.driver.get(url)
        self.wait.until(EC.url_to_be(url))

    def check_balance(self):
        self.wait.until(EC.presence_of_element_located(self.PROFILE)).click()
        self.wait.until(EC.presence_of_element_located(self.PROFILE_MENU))
        balanceText = (self.driver.find_element(*self.BALANCE).text.split(" ")[2])
        print("balance:" + balanceText)
        balance_count = int(balanceText)

    def logout(self):
        self.wait.until(EC.presence_of_element_located(self.PROFILE))
        menu = self.driver.find_element(*self.PROFILE)
        logout_user = self.driver.find_element(*self.LOGOUT_MENU)
        self.action.click(menu) \
            .move_to_element(logout_user) \
            .click(logout_user) \
            .perform()

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )
