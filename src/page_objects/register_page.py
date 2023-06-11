
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from src.page_objects.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver: WebDriver, wait_driver: WebDriverWait):
        super(RegisterPage, self).__init__(driver, wait_driver)

    def registrarse1(self, firstname: str, lastname: str, email: str, telephone: str, password: str, confirm: str):
        self.element("firstname_input").wait_clickable().send_keys(firstname)
        self.element("lastname_input").wait_clickable().send_keys(lastname)
        self.element("email_input").wait_clickable().send_keys(email)
        self.element("telephone_input").wait_clickable().send_keys(telephone)
        self.element("password_input").wait_clickable().send_keys(password)
        self.element("confirm_input").wait_clickable().send_keys(confirm)
        self.element("agree_btn").wait_clickable().click()
        self.element("confirm_btn").wait_clickable().click()

    def get_warning_message(self):
        return self.element("warning_message").wait_visible().text
