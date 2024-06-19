import allure

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    EMAIL_FIELD = ("xpath", "//*[@data-test='email']")
    PASSWORD_FIELD = ("xpath", "//*[@data-test='password']")
    LOGIN_BUTTON = ("xpath", "//*[@data-test='submit-form']")

    @allure.step("Enter email")
    def enter_email(self, email):
        self.wait.until(EC.element_to_be_clickable(self.EMAIL_FIELD)).clear()
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click on login button")
    def click_login_button(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    @allure.step("Login")
    def login(self, url, email, password):
        self.open(url)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
